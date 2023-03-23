from django.shortcuts import render
from .models import addtobag
from django.contrib.auth.models import User,auth
from PRODUCT.models import P_Details
from ADD_TO_CART.models import addtobag
from django.http import HttpResponseRedirect
# Create your views here.
def bag(request):
    u_id=request.user
    bag_detail=addtobag.objects.filter(user_id=u_id.id)
    #prod_detail=Wishlist.objects.select_related()
    return render(request,'shop-cart.html',{'items':bag_detail})

def proceed_checkout(request):
    u_id=request.user
    checkout_detail=addtobag.objects.filter(user_id=u_id.id)
    return render(request,'Checkout_Try.html',{'items':checkout_detail})