from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class AddFair(models.Model):
    zone=models.CharField(max_length=30)
    distance=models.CharField(max_length=30)
    fair=models.CharField(max_length=30)

    class Meta:
        db_table="add_fair"
class AddStationDetails(models.Model):
    add_image=models.ImageField(upload_to='station/')
    station_name=models.CharField(max_length=100)
    station_address=models.CharField(max_length=100)
    platform_type=models.CharField(max_length=30)
    distance=models.CharField(max_length=30)
    number_1=models.CharField(max_length=80)
    number_2=models.CharField(max_length=80)

    class Meta:
        db_table="station_details"
class AdminLogin(models.Model):
    user_name=models.CharField(max_length=40)
    password=models.CharField(max_length=50)

    class Meta:
        db_table="admin_login"