from django.db import models
from DASHBOARD.models import Customer_details

# Create your models here.
class Cat(models.Model):
    cat_id=models.IntegerField(primary_key=True)
    cat_name=models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name

class SubCat(models.Model):
    subcat_id=models.IntegerField(primary_key=True)
    cat_id=models.ForeignKey('Cat',default=0,on_delete=models.SET_DEFAULT)
    subcat_name=models.CharField(max_length=50)

    def __str__(self):
        return self.subcat_name
    
    
class P_Details(models.Model):
    product_id=models.IntegerField(primary_key=True)
    subcat_id=models.ForeignKey('SubCat',default=0,on_delete=models.SET_DEFAULT)
    offer_id=models.ForeignKey('Offer',default=0,on_delete=models.SET_DEFAULT)
    p_name=models.CharField(max_length=50)
    p_price=models.IntegerField()
    p_label=models.CharField(max_length=20,default="NEW")
    p_qty=models.IntegerField(null='True',blank=True)
    p_type=(
        ('Kurti','Kurti'),
        ('Kurti Set','Kurti Set'),
        ('Lehenga','Lehenga'),
        ('Dress','Dress'),
        ('Cosmetic','Cosmetic'),
        ('Footwear','Footwear'),
        ('Bags','Bags')
    )
    p_type=models.CharField(max_length=30,default="Kurti",choices=p_type,blank=True)
    p_fabric=models.CharField(max_length=30,null='True',blank=True)
    p_size=models.CharField(max_length=30,null='True',blank=True)
    p_img=models.ImageField(upload_to='Products',null='True',blank=True)
    p_img1=models.ImageField(upload_to='Products',null='True',blank=True)
    p_img2=models.ImageField(upload_to='Products',null='True',blank=True)
    p_img3=models.ImageField(upload_to='Products',null='True',blank=True)
    p_desc=models.CharField(max_length=100,null='True',blank=True)
    p_color=models.CharField(max_length=50,null='True',blank=True)
    p_filter=models.CharField(max_length=20,default=0,null='True',blank=True)
    p_brand=models.CharField(max_length=20,null='True',blank=True)
    Csmtc_type=(
        ('Foundation','Foundation'),
        ('Concealer','Concealer'),
        ('Primer','Primer'),
        ('Lipstick','Lipstick'),
        ('Compact','Compact')
    )

    Csmtc_type=models.CharField(max_length=30,default="Foundation",choices=Csmtc_type,blank=True)
    Acs_type=(
        ('Neckpiece','Neckpiece'),
        ('Rings','Rings'),
        ('Bangles','Bangles'),
        ('Earings','Earings')
    )

    Acs_type=models.CharField(max_length=30,default="Neckpiece",choices=Acs_type,blank=True)
    footWear_type=(
        ('Slipper','Slipper'),
        ('Heal','Heals'),
        ('Sandals','Sandals')
    )

    footwear_type=models.CharField(max_length=30,default="Slipper",choices=footWear_type,blank=True)     
    purse_type=(
        ('Wallet','Wallet'),
        ('Clutches','Clutches'),
        ('Waistbag','Waistbag')
    )

    purse_type=models.CharField(max_length=30,default="Clutches",choices=purse_type,blank=True)
    def __str__(self):
        return self.p_name

class Add_to_cart(models.Model):
    cart_id=models.IntegerField(primary_key=True)
    cust_id=models.ForeignKey('DASHBOARD.Customer_details',default=0,on_delete=models.SET_DEFAULT )
    p_id=models.ForeignKey('P_Details',default=0,on_delete=models.SET_DEFAULT )
    cart_qty=models.IntegerField(default=1)    


class Offer(models.Model):
    offer_id=models.IntegerField(primary_key=True)
    offer_name=models.TextField(max_length=30)
    offer_desc=models.TextField(max_length=150)
    offer_start_date=models.DateField()
    offer_end_date=models.DateField()    

