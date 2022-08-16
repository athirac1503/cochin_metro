from pickle import TRUE
from time import time
from django.db import models
from datetime import date
from datetime import datetime

from adminapp.models import AddStationDetails
# Create your models here.
class UserRegistration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    class Meta:
        db_table="user_signup"

class BookTicket(models.Model):
    ticket_id=models.ForeignKey(AddStationDetails,on_delete=models.CASCADE,null=True)
    ticket_type=models.CharField(max_length=20)
    ticket_from=models.CharField(max_length=40)
    ticket_to=models.CharField(max_length=40)
    no_passenger=models.BigIntegerField()
    date=models.CharField(max_length=20,null=True)
    time=models.CharField(max_length=20,null=True)
    user_id=models.ForeignKey(UserRegistration, on_delete=models.CASCADE,null=True)


    class Meta:
        db_table="ticket_book"

class Contact(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    contact_id=models.ForeignKey(UserRegistration, on_delete=models.CASCADE,null=True)
    reply=models.CharField(max_length=100,default='',null=True)

    class Meta:
        db_table="contact_us"


