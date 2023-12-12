from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import*

from logging import PlaceHolder
from django.contrib.auth.forms import PasswordChangeForm


# Customer register 

class UserForm(UserCreationForm):
    
    password1=forms.CharField(label='Enter Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    
    email = forms.EmailField(
        label=('Enter Email ID'),
        max_length=254,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email-Id'})
    )

    contact = forms.IntegerField(
        label=('Contact No'),
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Contact'})
    )
    
    class Meta:
        model = User
        fields =['first_name','last_name','email','contact','username','password1','password2']
        labels = {
            'first_name':'Enter First Name',
            'last_name':'Enter last name',
            'email':'Enter Email ID',
            'contact':'Contact No',
            'username':'Enter UserName',
            
        }

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last Name'}),
        }

# Customer login 

class CustomerLogin(AuthenticationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['Username']
        labels = {
            'password':'Password'
        }

#---------------------------------------------------------------------------

# Admin Login

class AdminLogin(AuthenticationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

    class Meta:
        model = User
        fields = ['Username']
        labels = {
            'password':'Password'
        }


#----------------------------------------------------------------


# Add car

class Addcarform(forms.ModelForm):
    class Meta:
        model=Addcar
        fields=['car_name','location','image','capacity','rent','is_available','cat']

        labels = {
            'car_name':'Car Name',
            'location':'City',
            'image':'Car Image',
            'capacity':'Number Of Seats',
            'is_available':'Car Status',
            'rent':'Rent (Per Day)',

        }

        widgets={
        'car_name':forms.TextInput(attrs={'class':'form-control'}),
        'location':forms.TextInput(attrs={'class':'form-control'}),
        'image':forms.FileInput(attrs={'class':'form-control'}),
        'capacity':forms.NumberInput(attrs={'class':'form-control'}),
            
        'rent':forms.NumberInput(attrs={'class':'form-control'}),
        'is_available':forms.TextInput(attrs={'class':'form-control'}),
        'cat':forms.Select(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        cat = kwargs.pop('cat', None)
        super(Addcarform, self).__init__(*args, **kwargs)
        if cat:
            self.fields ['cat'].queryset = cat

    
#----------------------------------------------------------------
    

# Contact form

class ContactForm(forms.ModelForm):
       
    class Meta:
        model = Contact
        fields = ['name', 'email', 'location' , 'message']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':' Enter Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':' Enter Email'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':' Enter City'}),
            'message':forms.TextInput(attrs={'class':'form-control','placeholder':' Message'})
            
        }

#-------------------------------------------------------------------------------------


# Update Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email ID',
            'username': 'Username',
            
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

#-------------------------------------------------------------------------------------

# customer password change


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
  

#-------------------------------------------------------------------------------------


# car book

from django.core.exceptions import ValidationError
from django.utils import timezone

class Carbookingform(forms.ModelForm):

    def clean_check_in_date(self):
        check_in_date = self.cleaned_data.get('check_in_date')
        today = timezone.now().date()

        if today > check_in_date or (check_in_date - today).days > 5:
            raise forms.ValidationError("Check-in date must be today or within the next 5 days.")

        return check_in_date

    def clean_check_out_date(self):
        check_out_date = self.cleaned_data.get('check_out_date')
        today = timezone.now().date()

        if today > check_out_date or (check_out_date - today).days > 5:
            raise forms.ValidationError("Check-out date must be today or within the next 5 days.")

        return check_out_date
    

    class Meta:
        model = carbooking  
        fields = ['pick_up_point', 'destination_point', 'check_in_date', 'check_out_date', 'no_of_persons', 'name', 'email', 'contact']
        labels = {
            'pick_up_point': 'Pick Up Point',
            'destination_point':'Destination Point',
            'check_in_date':'Check in Date',
            'check_out_date':'Check out Date',
            'no_of_persons':'No of Persons',
            'name':'Name',
            'email':'Email',
            'contact':'Contact',
            
            
        }

        widgets = {
                'pick_up_point': forms.TextInput(attrs={'class':'form-control'}),
                'destination_point': forms.TextInput(attrs={'class':'form-control'}),
                'check_in_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'check_out_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'no_of_persons': forms.NumberInput(attrs={'class':'form-control'}),
                'name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                'contact':forms.NumberInput(attrs={'class':'form-control'}),
               
            }

    


#----------------------------------------------------------------


'''
    def clean_check_in_date(self):
        check_in_date = self.cleaned_data.get('check_in_date')
        if check_in_date < timezone.now().date():
            raise forms.ValidationError("Check-in date cannot be in the past.")
        return check_in_date

    def clean_check_out_date(self):
        check_out_date = self.cleaned_data.get('check_out_date')
        if check_out_date < timezone.now().date():
            raise forms.ValidationError("Check-out date cannot be in the past.")
        return check_out_date
'''




















