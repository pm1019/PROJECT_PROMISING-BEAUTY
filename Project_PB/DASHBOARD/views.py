from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer_details
# Create your views here.
def DASHBOARD(request):
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

        cst_id=Customer_details.objects.only('cust_id').count()
        cst_id=cst_id+1

        user=Customer_details(cust_id=cst_id,cust_name=cust_name,cust_surname=cust_surname,cust_phoneno=cust_phoneno,cust_address1=cust_address1,cust_address2=cust_address2,cust_postcode=cust_postcode,cust_state=cust_state,cust_area=cust_area,cust_emailid=cust_emailid,cust_country=cust_country)
        user.save();
        print('user created')
        return redirect('dash/dashboard')

    else:
        return render(request,'Dashboard_Customer.html')    

    