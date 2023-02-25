from django.shortcuts import render
from PRODUCT.models import P_Details
from .models import details

# Create your views here.
def orders(request):
    Prods=details.objects.all()
    print (Prods)
    return render(request,'orderdetail.html',{'Prods':Prods})
    
    
    