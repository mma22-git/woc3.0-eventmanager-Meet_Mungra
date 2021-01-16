from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):

    name= models.CharField(max_length=30)
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


     