from django.db import models


class Student(models.Model):
    """Database model for students"""
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField()


class Mark(models.Model):
    """Database model for marks""" 
    mark = models.FloatField()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

