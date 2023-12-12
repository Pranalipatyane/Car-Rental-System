
from django.contrib import admin
from django.urls import path
from . import views


from django.contrib.auth import views as auth_views




urlpatterns = [
    path('',views.home,name='home'),

# home page
    path("about/",views.about,name="about"),
    path("terms/",views.terms,name="terms"),
    path("privacy/",views.privacy,name="privacy"),
    path("service/",views.service,name="service"),

#-------------------------------------------------------------------------

# home page - contact page
    path("contact_view/",views.contact_view,name="contact_view"),

#-------------------------------------------------------------------------

# search car
    #path("search/", views.search, name="search"),


    path('api/search/', views.CarSearchAPIView.as_view(), name='search'),


#-------------------------------- Customer Page ----------------------------------------

# customer register
    path("customer_register/",views.customer_register.as_view(),name="customer_register"),

# customer login
    path("customer_login/",views.customer_login.as_view(),name="customer_login"),

# customer homepage
    path("customer_homepage/",views.customer_homepage,name="customer_homepage"),


#---------------------------------------------------------------------------------

# customer page - show car
    path("show_car/",views.show_car,name="show_car"),
    path("cat/<int:id>/",views.cat_view,name="cat"),

#---------------------------------------------------------------------------------

# customer page - packages

   path("imagica/",views.imagica,name="imagica"),
   path("pune/",views.pune,name="pune"),
   path("lavasa/",views.lavasa,name="lavasa"),
   path("lonavala/",views.lonavala,name="lonavala"),

#---------------------------------------------------------------------------------

# customer page - packages
    path("package_cust/",views.package_cust,name="package_cust"),
  
#---------------------------------------------------------------------------------

# customer page - car booking
    path('book-car/<int:id>/',views.CarbookingView.as_view(),name='book_car'),
   
#---------------------------------------------------------------------------------

# customer page - show booking details
    path("show_booking/",views.show_booking,name="show_booking"),
    

# customer page - cancel booking 
    path('your_booking/<int:id>/', views.your_booking, name='your_booking'),


# customer page - booking
    #path("booking_form/",views.booking_view,name="booking_form"),


# customer page - Update booking details
    path('edit_booking/<int:id>/', views.EditCarbookingView.as_view(), name='edit_booking'),
    

# customer page - confirm booking page
    path('booking_confirmation/<int:id>/', views.BookingConfirmationView.as_view(), name='booking_confirmation'),


#---------------------------------------------------------------------------------

# customer profile view
    path("profile/", views.view_profile, name="view_profile"),

#---------------------------------------------------------------------------------

# customer profile update
    #path("profile-update/", views.profile_update, name="profile_update"),
    path("profile-update/", views.profile_update.as_view(), name="profile_update"),

#---------------------------------------------------------------------------------

# customer password change
    #path("change_password/",views.change_password, name="change_password"),
    path("change_password/",views.change_password, name="change_password"),

#---------------------------------------------------------------------------------

# customer - forgot password

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),

#---------------------------------------------------------------------------------



#------------------------------ Admin Page ----------------------------------------


# admin login
    path("admin_login/",views.admin_login.as_view(),name="admin_login"),

# admin homepage
    path("admin_homepage/",views.admin_homepage,name="admin_homepage"),

#---------------------------------------------------------------------------------

# admin page - add car

    #path("add_car/", views.add_new_car, name="add_car"),
    path("add_car/",views.add_new_car.as_view(),name="add_car"),

    #path('api/cars/', AddCarAPI.as_view(), name='add_car'),
#---------------------------------------------------------------------------------

# admin page - all cars
    path("all_cars/", views.all_cars, name="all_cars"),

#---------------------------------------------------------------------------------

# admin page - delete car
    path("delete_car/<int:id>/", views.delete_car, name="delete_car"),

#---------------------------------------------------------------------------------

# admin page - update car
    path("update_car/<int:id>/",views.update_car.as_view(),name="update_car"),

#---------------------------------------------------------------------------------
    
# admin page - show car booking details
    path("custom_admin/", views.custom_admin_page, name="custom_admin_page"),

#---------------------------------------------------------------------------------

#admin page - delete car booking details
    path("delete_booking/<int:id>/", views.delete_booking, name="delete_booking"),

#---------------------------------------------------------------------------------

# admin page - show customer details
    path("customer_details/",views.customer_details,name="customer_details"),

#---------------------------------------------------------------------------------

# admin page - show contact details
    path("contact_details/",views.contact_details,name="contact_details"),
    
#---------------------------------------------------------------------------------

# admin page - delete contact details
    path("delete_contact/<int:id>/", views.delete_contact, name="delete_contact"),

#---------------------------------------------------------------------------------

# admin page - booking cancel
    path('cancel_booking/<int:id>/', views.cancel_booking_view, name='cancel_booking'),

#-----------------------------------------------------------------------------------------------------
   
# logout
    path("signout/",views.signout,name="signout"),



    
]
