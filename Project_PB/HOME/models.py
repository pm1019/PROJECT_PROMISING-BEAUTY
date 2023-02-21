from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id=models.IntegerField(primary_key=True)
    name=models.TextField(max_length=30)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=300)