from django.db import models
from DASHBOARD.models import Customer_details
from PRODUCT.models import P_Details
from django.contrib.auth.models import User, auth
# Create your models here.
class addtobag(models.Model):
    bag_id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    product=models.ForeignKey(P_Details,on_delete=models.CASCADE,default=0)

    def prod_img(self):
        return self.product.p_img
    def prod_price(self):
        return self.product.p_price
    def prod_name(self):
        return self.product.p_name