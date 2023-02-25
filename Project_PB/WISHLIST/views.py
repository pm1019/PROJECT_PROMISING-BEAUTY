from django.shortcuts import render
from .models import Wishlist
from django.contrib.auth.models import User,auth
from PRODUCT.models import P_Details
from WISHLIST.models import Wishlist
from django.http import HttpResponseRedirect
# Create your views here.
def wishlist(request):
    u_id=request.user
    wish_detail=Wishlist.objects.filter(user_id=u_id.id)
    #prod_detail=Wishlist.objects.select_related()
    return render(request,'Wishlist.html',{'items':wish_detail})