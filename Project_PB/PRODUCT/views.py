from django.shortcuts import render,redirect,reverse
from .models import P_Details,Customer_details
from django.contrib.auth.models import User
from ADD_TO_CART.models import addtobag
from WISHLIST.models import Wishlist
from django.http import HttpResponseRedirect

# Create your views here.
def product(request):
    Prods=P_Details.objects.all()
    return render(request,'shop.html',{'Prods':Prods})

def prods_detail(request,id):
    detail=P_Details.objects.get(p_id=id)
    return render(request,'product-details.html',{'data':detail})



def addToWishlist(request,id):
    prod=id
    u_id=request.user
    w_id=Wishlist.objects.only('id').count()
    w_id=w_id+1
    if Wishlist.objects.filter(product_id=prod,user_id=u_id.id).exists():
        return redirect('show_wishlist')
    else:  
        Wishlist.objects.create(wishlist_id=w_id,product_id=prod,user_id=u_id.id)
        return redirect('show_wishlist')     
    
def show_wish(request):
    u_id=request.user
    wish_data=Wishlist.objects.filter(user_id=u_id.id)
    context={
        'wish_data':wish_data
    }
    return render(request,'Wishlist.html',context)

def addTobag(request,id):
    prod=id
    u_id=request.user
    b_id=addtobag.objects.only('bag_id').count()
    b_id=b_id+1
    if addtobag.objects.filter(product_id=prod,user_id=u_id.id).exists():
        return redirect('show_bag')
    else:  
        addtobag.objects.create(bag_id=b_id,product_id=prod,user_id=u_id.id)
        return redirect('show_bag')         

def show_bag(request):
    u_id=request.user
    bag_data=addtobag.objects.filter(user_id=u_id.id)
    context={
        'bag_data':bag_data
    }
    return render(request,'shop-cart.html',context)        

def search(request):
    src=request.GET["prod_name"]
    if src=='':
        return redirect('shop')
    else:
        data=P_Details.objects.filter(p_name=src)
        return render(request,'shop.html',{'data':data})
