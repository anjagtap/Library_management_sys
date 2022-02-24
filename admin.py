from django.contrib import admin
from .models import data, Record


# Register your models here.
@admin.register(data)
class dataadmin(admin.ModelAdmin):
    list_display = ('id','book_name','author_name','price')

@admin.register(Record)
class recordadmin(admin.ModelAdmin):
    list_display = ['id','ename','email','mobile','password','dob']