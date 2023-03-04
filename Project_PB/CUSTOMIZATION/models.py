from django.db import models

# Create your models here.
class Dress(models.Model):
    custom_dress_id=models.IntegerField(primary_key=True)
    custom_size=models.CharField(max_length=10)
    custom_fabric=models.CharField(max_length=20)
    custom_colour=models.CharField(max_length=20)