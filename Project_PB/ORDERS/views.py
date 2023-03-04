from django.shortcuts import render
from PRODUCT.models import P_Details
from .models import details

# Create your views here.
def orders(request):
    Prods=details.objects.all()
    print (Prods)
    return render(request,'orderdetail.html',{'Prods':Prods})
    
#def total(request):
    val1=int(request.GET["amount"])
    val2=int(request.GET["Charge"])    
    val3=int(request.GET["recvd"])
    cst=val1+(val2/100)
    result=val3-cst

    return render(request,'Money_Transfer.html',{'res':result})    
    