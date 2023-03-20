from django.shortcuts import render,redirect,reverse
from .models import P_Details,Customer_details,Cat,SubCat
from django.contrib.auth.models import User
from ADD_TO_CART.models import addtobag
from WISHLIST.models import Wishlist
from django.http import HttpResponseRedirect


# Create your views here.
def product(request):
    Prods=P_Details.objects.all()
    Data={
        'Prods':Prods
    }
    return render(request,'shop.html',Data)

def prod_detail(request,id):
    detail=P_Details.objects.get(product_id=id)
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

def remove_wish(request,id):
    u_id=request.user
    items=Wishlist.objects.get(product_id=id,user_id=u_id.id)        
    items.delete()
    return redirect('show_wishlist') 

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
    
def remove_bag(request,id):
    u_id=request.user
    item=addtobag.objects.get(product_id=id,user_id=u_id.id)
    item.delete()
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
        data=P_Details.objects.filter(p_name__icontains=src)
        return render(request,'shop.html',{'data':data})

def categories(request):
    src=request.GET['type']
    Prods=P_Details.objects.filter(p_fabric=src)
    Data={
        'Prods':Prods
    }
    return render(request,'shop.html',Data)

    
def low_to_high(request):
    cats=Cat.objects.all()
    subcats=SubCat.objects.all()
    lowToHigh=P_Details.objects.all().order_by('p_price')
    Data={
        'Prods':lowToHigh,
        'cats':cats,
        'subcats':subcats
    }
    return render(request,'shop.html',Data)

def high_to_low(request):
    cats=Cat.objects.all()
    subcats=SubCat.objects.all()
    lowToHigh=P_Details.objects.all().order_by('-p_price')
    Data={
        'Prods':lowToHigh,
        'cats':cats,
        'subcats':subcats
    }
    return render(request,'shop.html',Data)        