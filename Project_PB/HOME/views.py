from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

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

