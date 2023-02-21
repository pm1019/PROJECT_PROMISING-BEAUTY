from django.shortcuts import render,redirect
from .models import P_Details,Add_to_cart,Customer_details
from django.contrib.auth.models import User

# Create your views here.
def product(request):
    Prods=P_Details.objects.all()
    return render(request,'shop.html',{'Prods':Prods})

def prods_detail(request,id):
    detail=P_Details.objects.get(p_id=id)
    return render(request,'product-details.html',{'data':detail})

