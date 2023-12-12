from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

   
#-----------------------------------------------------------

# category 

class categoryModel(models.Model):
    car_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.car_name
    
#-----------------------------------------------------------

# Add car

class Addcar(models.Model):
    car_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    is_available = models.CharField(max_length=100,default=True)
    rent = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True,validators=[MinValueValidator(0)])
    cat = models.ForeignKey(categoryModel, on_delete=models.CASCADE)

   
    def __str__(self):
        return self.car_name


#-----------------------------------------------------------


# Contact

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

#-----------------------------------------------------------

# Car Booking

class carbooking(models.Model):

    addcar=models.ForeignKey(Addcar,related_name="car_booking",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name="user_booking",on_delete=models.CASCADE)
    pick_up_point = models.CharField(max_length=100)
    destination_point = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    no_of_persons = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(10)], max_length = 10)
    is_confirmed = models.BooleanField(default=True)


#-----------------------------------------------------------




































#-----------------------------------------------------------

'''
# Car Booking

class Booking(models.Model):

    CAR_CHOICES = (
        ('Tata Zest', 'Tata Zest'),
        ('Maruti Dzire', 'Maruti Dzire'),
        ('Swift Dzire', 'Swift Dzire'),
        ('Toyota Etios', 'Toyota Etios'),
        ('Toyota Innova', 'Toyota Innova'),
        ('Maruti Ertiga', 'Maruti Ertiga'),
        ('Hyundai Xcent', 'Hyundai Xcent'),
        
    )
   
    pick_up_point = models.CharField(max_length=100)
    destination_point = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    car_type = models.CharField(max_length=50, choices=CAR_CHOICES)
    no_of_persons = models.IntegerField()
   
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(10)], max_length = 10)
    is_confirmed = models.BooleanField(default=True)

'''
#-----------------------------------------------------------
