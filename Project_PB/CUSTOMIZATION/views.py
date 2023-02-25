from django.shortcuts import render

# Create your views here.
def custom(request):
    return render(request,'customizationhome.html')

def hoops(request):
    return render(request,'hoop.html')