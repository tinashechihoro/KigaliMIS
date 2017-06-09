from django.db import models

# Student model
class Student(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=100,help_text="First name")
    middle_name = models.CharField(max_length=100,help_text="Middle name")
    last_name = models.CharField(max_length=100,help_text="Last name")
    gender = models.CharField(max_length=1, choices=GENDER)

