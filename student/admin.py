from django.contrib import admin
from . import models

@admin.register(models.Student)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','roll_number', 'date_of_birth')

@admin.register(models.Mark)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'student')




