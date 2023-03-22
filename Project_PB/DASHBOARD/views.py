from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer_details
# Create your views here.
def dash_cust_details(request):
    if request.method == 'POST':
        cust_name=request.POST['Name']
        cust_surname=request.POST['Surname']
        cust_phoneno=request.POST['Mobile Number']
        cust_address1=request.POST['Address home']
        cust_address2=request.POST['Address office']
        cust_postcode=request.POST['Postcode']
        cust_state=request.POST['State']
        cust_area=request.POST['Area']
        cust_emailid=request.POST['Email ID']
        cust_country=request.POST['Country']

        u_id=request.user
        cst_id=Customer_details.objects.only('cust_id').count()
        cst_id=cst_id+1

        if Customer_details.objects.filter(user_id=u_id.id).exists():
            obj=Customer_details.objects.get(user_id=u_id.id)
            obj_user=User.objects.get(id=u_id.id)
            obj.cust_name=cust_name
            obj.cust_phoneno=cust_phoneno
            obj.cust_surname=cust_surname
            obj_user.first_name=cust_name
            obj_user.last_name=cust_surname
            obj.save()
            obj_user.save()
            return redirect('show_data')
        else:
            u_id=request.user
            cust_detail=Customer_details(cust_id=cst_id,user_id=u_id.id,cust_name=cust_name,cust_surname=cust_surname,cust_phoneno=cust_phoneno,cust_address1=cust_address1,cust_address2=cust_address2,cust_postcode=cust_postcode,cust_state=cust_state,cust_area=cust_area,cust_emailid=cust_emailid,cust_country=cust_country)
            cust_detail.save();
            print('user created')
            return redirect('show_data')

    else:
        return render(request,'Dashboard_Customer.html') 

def show(request):
    u_id=request.user
    cust_detail=Customer_details.objects.get(user_id=u_id.id)
    return render(request,'Dashboard_Customer.html',{'cust_detail':cust_detail})  

def profile_error(request):
    msg="Your Profile can't be Visible, Please Login for it..!!"
    return render(request,'error.html',{'msg':msg}) 

def order_error(request):
    msg="Your Orders can't be Visible, Please Login for it..!!"
    return render(request,'error.html',{'msg':msg})

def wish_error(request):
    msg="Your Wishlist can't be Visible, Please Login for it..!!"
    return render(request,'error.html',{'msg':msg})

def wish_icon_error(request):
    msg="Can't Add this Product to Wishlist, Please Login for it..!!"
    return render(request,'error.html',{'msg':msg})

def bag_error(request):
    msg="Your Cart can't be Visible, Please Login for it..!!"
    return render(request,'error.html',{'msg':msg})

def bag_icon_error(request):
    msg="Can't Add this Product to Cart, Please Login for it..!!"
    return render(request,'error.html',{'msg':msg})

    