from django.contrib import admin
from .models import*

# Register your models here.


admin.site.register(categoryModel)

admin.site.register(Addcar)
class addcar(admin.ModelAdmin):
    list_display=['car_name','image','capacity','location','is_available','rent','cat']


admin.site.register(Contact)
class contact(admin.ModelAdmin):
    list_display=['name','email','location','message']


admin.site.register(carbooking)
class booking(admin.ModelAdmin):
    list_display=['addcar','user','pick_up_point','destination_point','check_in_date','check_out_date','no_of_persons','name','email','contact','is_confirmed']

