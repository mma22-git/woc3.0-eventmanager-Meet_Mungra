from django.db import models
from datetime import datetime


class Event(models.Model):

    name= models.CharField(max_length=30, unique=True)
    location= models.CharField(max_length=200)
    link= models.URLField(blank=True)
    from_date= models.DateField()
    from_time= models.TimeField()
    to_date= models.DateField()
    to_time= models.TimeField()
    Reg_deadline= models.DateField()
    deadline_time= models.TimeField()
    email= models.EmailField(max_length=100)
    password= models.CharField(max_length=20)
    description= models.TextField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    c=(
        ('I','Individual'),('G','Group')
    )
    Name=models.CharField(max_length=30)
    Contact=models.IntegerField(max_length=10)
    Email=models.EmailField(max_length=100)
    Checked=models.CharField(max_length=1000, default='Some')
    Reg_type=models.CharField(max_length=30,choices=c)
    No_of=models.CharField(max_length=10,default="0")

    def __str__(self):
        return self.Name


     