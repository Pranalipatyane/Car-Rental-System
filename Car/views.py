from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .forms import*
from .models import*
from django.views import View
from django.shortcuts import get_object_or_404

from django.contrib.auth import update_session_auth_hash

from django.core.mail import send_mail

from django.db.models import Q

# Create your views here.


def home(request):
    car = Addcar.objects.all()
    return render(request, 'home.html',{'car':car})

def about(request):
    return render(request,"about.html")

def terms(request):
    return render(request,"terms.html")

def privacy(request):
    return render(request,"privacy.html")

def service(request):
    return render(request,"service.html")


#---------------------------------------------------------------------------

# contact


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification to the customer
            subject = 'Contact Form Submission'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\nMessage: {form.cleaned_data["message"]}'
            from_email = contact.email
            recipient_list = ['example@gmail.com']

            send_mail(subject, message, from_email, recipient_list)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

   
#-----------------------------------------------------------------

# Search car

from .serializers import AddcarSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer

class CarSearchAPIView(generics.ListAPIView):
    serializer_class = AddcarSerializer
    template_name = 'search_results.html'

    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('query', '')
        car_id = self.kwargs.get('id')  # Retrieve the 'id' parameter from the URL

        # Check if 'id' is provided in the request body
        if not car_id and 'id' in request.data:
            car_id = request.data['id']

        # If 'id' is provided, get a specific car
        if car_id is not None:
            cars = Addcar.objects.filter(id=car_id)
        elif query:
            cars = Addcar.objects.filter(Q(car_name__icontains=query) | Q(location__icontains=query))
        else:
            cars = Addcar.objects.all()

        print(f"Query: {query}")
        print(f"Car ID: {car_id}")
        print(f"Cars: {cars}")

        # If it's an API request, return JSON
        if self.request.accepted_renderer.format == 'json':
            serializer = self.get_serializer(cars, many=True)
            return Response(serializer.data)

        # If it's an HTML request, render the HTML page with the search results
        return render(request, self.template_name, {'cars': cars})




'''
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('query', '')
        cars = Addcar.objects.filter(Q(car_name__icontains=query) | Q(location__icontains=query))

        print(f"Query: {query}")
        print(f"Cars: {cars}")

        if self.request.accepted_renderer.format == 'json':
            serializer_data = self.get_serializer(cars, many=True).data
            return Response(serializer_data)

        return render(request, self.template_name, {'cars': cars})
'''


'''
# search carname and city name
def search(request):
    query = request.GET.get('query', '')  # Set default value to empty string if query parameter is None
    cars = []

    if query:
        cars = Addcar.objects.filter(Q(car_name__icontains=query) | Q(location__icontains=query))

    print(f"Query: {query}")
    print(f"Cars: {cars}")
    return render(request, 'search_results.html', {'cars': cars})


# search only car name
def search(request):
    if request.method == "POST":
        x = request.POST.get('search', '')
        search_obj = Addcar.objects.filter(car_name__icontains=x)
        return render(request, 'search_results.html', {'search_obj': search_obj})
  ''' 


#--------------------------------------------------------------------------------------


#---------------------- customer page -------------------------------------------

# customer register
 
class customer_register(View):
    def get(self,request):
        f = UserForm()
        return render(request, 'customer_register.html', {'f': f})
    
    def post(self,request):
        if request.method == 'POST':
            f = UserForm(request.POST)
            if f.is_valid():
                f.save()
                messages.success(request, 'Account created successfully')
                return redirect('customer_login')
            else:
                print(f.errors)  
                messages.warning(request, 'Something Went Wrong')
                return redirect(to='customer_register')


# customer login

class customer_login(View):
    def get(self,request):
        f=CustomerLogin()
        return render(request,'customer_login.html',{'f':f})

    def post(self,request):
        if request.method=='POST':
            uname=request.POST['username']
            upass=request.POST['password']
            user=authenticate(request,username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect(to='customer_homepage')
            else:
                messages.warning(request,f' Something Went Wrong While Login ')
                return redirect(to='customer_login')

#---------------------------------------------------------------------------

# customer homepage

@login_required(login_url='/customer_login/') 
def customer_homepage(request):
    return render(request,"customer_homepage.html")

#---------------------------------------------------------------------------

# customer - show all cars

@login_required(login_url='/customer_login/') 

def show_car(request):
    category=categoryModel.objects.all()
    car=Addcar.objects.all()
    context={"category":category,"car":car}
    return render(request,'show_car.html',context)
    
def cat_view(request,id):
    category=categoryModel.objects.all()
    car=Addcar.objects.filter(cat=id)

    context={'category':category,'car':car}
    return render(request,'show_car.html',context)

#-----------------------------------------------------------------

# customer homepage - packages

def imagica(request):
    return render(request,'cust_package/adlabs_imagica.html')

def pune(request):
    return render(request,'cust_package/pune.html')

def lavasa(request):
    return render(request,'cust_package/lavasa.html')

def lonavala(request):
    return render(request,'cust_package/lonavala.html')


#-----------------------------------------------------------------

# customer page - packages
@login_required(login_url='/customer_login/') 

def package_cust(request):
    return render(request,'package_cust.html')

#-----------------------------------------------------------------

#-------------------------------------------------------------------------------------

# customer page - view customer profile
@login_required
def view_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


#------------------------------------------------------------------------------------

# customer page - customer profile update


class profile_update(View):
    def get(self,request):
        form = UserProfileForm(instance=request.user)
        return render(request, 'profile_update.html', {'form': form})
    
    def post(self,request):
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('customer_homepage')
            else:
                messages.error(request, 'Error updating your profile. Please correct the errors below.')



#-----------------------------------------------------------------

# customer page - customer password change

@login_required(login_url='/customer_login/') 
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile_update') 
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

#---------------------------------------------------------------------------------------------


# car booking by user

def calculate_total_rent(check_in_date, check_out_date, num_of_persons):
    num_days = (check_out_date - check_in_date).days
    totalRent = 400 * num_of_persons * num_days 
    return totalRent


class CarbookingView(View):
    def get(self,request,id):
        car=get_object_or_404(Addcar,id=id)
        if request.user.is_authenticated:
            form = Carbookingform()
            return render(request, 'Booking.html', {'car': car,'form': form})
        else:
            return redirect('show_car') 

    def post(self, request,id):
        car = get_object_or_404(Addcar, id=id)
        if request.user.is_authenticated:
            form = Carbookingform(request.POST)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.addcar = car
                booking.user = request.user
                booking.save()

                # Calculate total rent
                check_in_date = booking.check_in_date
                check_out_date = booking.check_out_date
                no_of_persons = booking.no_of_persons
                totalRent = calculate_total_rent(check_in_date,check_out_date,no_of_persons)

                # Send email notification to the customer
                subject = 'Car Booking Confirmation'
                message = f'Thank you for booking the {booking.addcar} from {booking.pick_up_point} to {booking.destination_point}.\n Your booking is confirmed from {booking.check_in_date} to {booking.check_out_date} with {booking.no_of_persons} member,\n Total is {totalRent}'
                from_email = 'example@gmail.com'  # Update this with your email address
                recipient_list = [booking.email]
                send_mail(subject, message, from_email, recipient_list)

                # Pass the car rent value to the template
                return render(request, 'booking_confirmation.html', {'booking': booking,'totalRent': totalRent})
    
            else:
                return render(request, 'Booking.html', {'car': car, 'form': form})
        else:
            return redirect('show_car')  
        
#---------------------------------------------------------------------------------------------

# customer page - show car booking details

def show_booking(request):
    if request.user.is_authenticated:
        user_bookings = carbooking.objects.filter(user=request.user)

        # Calculate total rent for each booking and add it to the context
        for booking in user_bookings:
            totalRent = calculate_total_rent(booking.check_in_date, booking.check_out_date, booking.no_of_persons)
            booking.totalRent = totalRent

        return render(request, 'show_details.html', {'user_bookings': user_bookings})
    else:
        return redirect('customer_homepage')
    

#---------------------------------------------------------------------------------------------

# customer page - cancel booking 

@login_required (login_url='/customer_login/')  
def your_booking(request,id):
    book=carbooking.objects.get(id=id)
    book.delete()
    return redirect('show_booking')

#---------------------------------------------------------------------------------------------

# customer page - update booking details

class EditCarbookingView(View):
    def get(self, request, id):
        booking = get_object_or_404(carbooking, id=id)
        form = Carbookingform(instance=booking)
        return render(request, 'edit_booking.html', {'form': form, 'booking': booking})

    def post(self, request, id):
        booking = get_object_or_404(carbooking, id=id)
        form = Carbookingform(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            
            return redirect('booking_confirmation', id=booking.id)  
        return render(request, 'edit_booking.html', {'form': form, 'booking': booking})

#--------------------------------------------------------------------------------

# customer page - confirm booking details

class BookingConfirmationView(View):
    def get(self, request, id):
        booking = get_object_or_404(carbooking, id=id)

        # Calculate total rent
        check_in_date = booking.check_in_date
        check_out_date = booking.check_out_date
        no_of_persons = booking.no_of_persons
        totalRent = calculate_total_rent(check_in_date,check_out_date,no_of_persons)

        return render(request, 'booking_confirmation.html', {'booking': booking, 'totalRent':totalRent})

#--------------------------------------------------------------------------------

# logout

def signout(request):
    logout(request)
    return redirect('home')

#---------------------------------------------------------------------------









#---------------------- admin page -------------------------------------------

# admin login


class admin_login(View):
    def get(self,request):
        f=CustomerLogin()
        return render(request,'admin_login.html',{'f':f})

    def post(self,request):
        if request.method=='POST':
            uname=request.POST['username']
            upass=request.POST['password']
            user=authenticate(request,username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect(to='admin_homepage')
            else:
                messages.warning(request,f' Something Went Wrong While Login ')
                return redirect(to='admin_login')

#---------------------------------------------------------------------------

# admin homepage

@login_required (login_url='/admin_login/')
def admin_homepage(request):
    return render(request, "admin_homepage.html")

#---------------------------------------------------------------------------

# admin page - add car


class add_new_car(View):
    def get(self,request):
        form = Addcarform()  
        return render(request, 'add_new_car.html', {'form': form})
    def post(self,request):
        if request.method == 'POST':
            form = Addcarform(request.POST, request.FILES, cat=categoryModel.objects.all())
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect('all_cars')
      


#---------------------------------------------------------------------------
        
# admin page - show all cars

@login_required (login_url='/admin_login/')
def all_cars(request):
    cars=Addcar.objects.all()
    context={'car':cars}
    return render(request,'all_cars.html',context)


#---------------------------------------------------------------------------

# admin page - Delete car

@login_required (login_url='/admin_login/')  
def delete_car(request,id):
    car=Addcar.objects.get(id=id)
    car.delete()
    return redirect('all_cars')

#---------------------------------------------------------------------------

# admin page - Update Car


class update_car(View):
    def get(self,request,id):
        pi=Addcar.objects.get(id=id)
        form=Addcarform(instance=pi)
        return render(request,'update_car.html',{'form':form})  
    def post(self,request,id):
        if request.method=='POST':
            pi=Addcar.objects.get(id=id)
            form=Addcarform(request.POST,request.FILES,instance=pi)
            if form.is_valid():
                form.save()
                return redirect('all_cars')

#---------------------------------------------------------------------------

# admin page - show car booking details  

def custom_admin_page(request):
    
    form = Carbookingform()
    m = carbooking.objects.all()

    for booking in m:
        totalRent = calculate_total_rent(booking.check_in_date, booking.check_out_date, booking.no_of_persons)
        booking.totalRent = totalRent
    return render(request, 'custom_admin_page.html', {'form':form,'m':m})

#---------------------------------------------------------------------------

# admin page - delete bookings

@login_required (login_url='/admin_login/')  
def delete_booking(request,id):
    booking=carbooking.objects.get(id=id)
    booking.delete()
    return redirect('custom_admin_page')

#-----------------------------------------------------------------

# admin page - show customer details

@login_required
def customer_details(request):
    cust = User.objects.all()
    return render(request, 'customer_details.html', {'cust': cust})

#-----------------------------------------------------------------

# admin page - show contact details

def contact_details(request):
    contact = Contact.objects.all()
    return render(request, 'contact_details.html', {'contact': contact})

#-----------------------------------------------------------------

# admin page - delete contact details

@login_required (login_url='/admin_login/')  
def delete_contact(request,id):
    contact=Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact_details')


#-----------------------------------------------------------------

# admin page - cancel booking car

@login_required(login_url='/admin_login/')
def cancel_booking_view(request, id):
    booking_instance = get_object_or_404(carbooking, id=id)

    # Check if booking is already confirmed
    if booking_instance.is_confirmed:
        # Send email notification to the customer about cancellation
        subject = 'Booking Cancellation Confirmation'
        message = f'Your booking for {booking_instance.addcar} from {booking_instance.pick_up_point} to {booking_instance.destination_point} has been canceled.\n Booking date : {booking_instance.check_in_date} to {booking_instance.check_out_date} with {booking_instance.no_of_persons} menber.'
        from_email = 'example@gmail.com'  # Update this with your email address
        recipient_list = [booking_instance.email]
        send_mail(subject, message, from_email, recipient_list)

        # Mark the booking as canceled
        booking_instance.is_confirmed = False
        booking_instance.save()

        messages.success(request, 'Booking canceled successfully.')
    else:
        messages.warning(request, 'Booking is already canceled.')

    return redirect('custom_admin_page')  


#-----------------------------------------------------------------



    


















