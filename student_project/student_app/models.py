from django.db import models
from django.db.models import (
    CharField,
    EmailField,
    IntegerField,
    TextField,
    ImageField,
    FileField,)

class Student(models.Model):
    Admission_option = (
        ('1','class 1'),
        ('2','class 2'),
        ('3','class 3'),
        ('4','class 4'),
        ('5','class 5'),
        ('6','class 6'),
        ('7','class 7'),
        ('8','class 8'),
        ('9','class 9'),
        ('10','class 10'),
        ('11','class 11'),
        ('12','class 12'),
    )

    Admission_No=CharField(max_length=50, blank=False)
    Full_name=CharField(blank=False, max_length=50)
    Email=EmailField(blank=False, max_length=100)
    Age=IntegerField()
    Class=CharField(max_length=50, choices=Admission_option)
    Description=TextField()
    Image=ImageField(upload_to='image/', null=True,blank=True)
    Marklist=FileField(upload_to='marklist/', null=True,blank=True)

def __self__(self):
    return self.Full_name

