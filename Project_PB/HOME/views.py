from django.shortcuts import render,redirect
from .models import Contact
from PRODUCT.models import P_Details

# Create your views here.
def home(request):
    Prods=P_Details.objects.all()
    Data={
        'Prods':Prods
    }
    return render(request,'index.html',Data)

def contact(request):
    return render(request,'contact.html')

def product(request):
    Prods=P_Details.objects.all()
    Data={
        'Prods':Prods
    }
    return render(request,'index.html',Data)

def SendContact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        cont_id=Contact.objects.only('contact_id').count()
        cont_id+=1
        contact=Contact(contact_id=cont_id,name=name,email=email,message=message)
        contact.save()
        return redirect('/')

def blog(request):
    return render(request,'blog.html')
    
def blogdetails(request):
    return render(request,'blog-details.html')    

def search(request):
    src=request.GET["prod_name"]
    if src=='':
        return redirect('shop')
    else:
        data=P_Details.objects.filter(p_name__icontains=src)
        return render(request,'shop.html',{'data':data})