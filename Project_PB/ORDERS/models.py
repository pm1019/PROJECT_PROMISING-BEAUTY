from django.db import models
from DASHBOARD.models import Customer_details
from PRODUCT.models import P_Details
from django.contrib.auth.models import User, auth

# Create your models here.
class details(models.Model):
    o_id=models.IntegerField(primary_key=True)
    cust_id=models.ForeignKey('DASHBOARD.Customer_details',on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    p_id=models.ForeignKey('PRODUCT.P_Details',on_delete=models.CASCADE)
    o_qty=models.IntegerField()
    o_netamount=models.IntegerField()
    o_date=models.DateField()
    o_details=models.CharField(max_length=100)
    o_status=models.BooleanField(default=False)


    def prod_img(self):
        return self.p_id.p_img
    def prod_price(self):
        return self.p_id.p_price
    def prod_name(self):
        return self.p_id.p_name
    def prod_color(self):
        return self.p_id.p_color    