from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Customer_details(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    cust_name=models.CharField(max_length=50)
    cust_surname=models.CharField(max_length=50)
    cust_phoneno=models.CharField(max_length=11)
    cust_address1=models.CharField(max_length=150)
    cust_address2=models.CharField(max_length=150)
    cust_postcode=models.CharField(max_length=10)
    cust_state=models.CharField(max_length=50)
    cust_area=models.CharField(max_length=50)
    cust_emailid=models.EmailField(max_length=50)
    cust_country=models.CharField(max_length=50)

class Delivery_details(models.Model):
    del_id=models.IntegerField(primary_key=True)
    del_name=models.CharField(max_length=50)
    del_surname=models.CharField(max_length=50)
    del_phoneno=models.IntegerField()
    del_address1=models.CharField(max_length=150)
    del_address2=models.CharField(max_length=150)
    del_postcode=models.IntegerField()
    del_state=models.CharField(max_length=50)
    del_area=models.CharField(max_length=50)
    del_emailid=models.EmailField(max_length=50)
    del_country=models.CharField(max_length=50)
    del_state=models.CharField(max_length=20)
    del_adharno=models.IntegerField()