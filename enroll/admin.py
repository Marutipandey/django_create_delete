from django.contrib import admin
from .models import simpleform
# Register your models here.
from .forms import loginform
@admin.register(simpleform)
class loginadminform(admin.ModelAdmin):
    list_display=['name','email','phone_number']