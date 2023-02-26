from django.shortcuts import render

# Create your views here.
def custom(request):
    return render(request,'customizationhome.html')

def hoops(request):
    return render(request,'hoop.html')

def bestperson(request):
    return render(request,'bestperson.html')

def bestperson1(request):
    return render(request,'1_bestperson_hoop.html')

def bestperson2(request):
    return render(request,'2_bestperson_hoop.html')

def namehoop(request):
    return render(request,'name_hoop.html')

def namehoop1(request):
    return render(request,'1_name_hoop.html')

def namehoop2(request):
    return render(request,'2_name_hoop.html')

def weddinghoop(request):
    return render(request,'weddinghoop.html')

def weddinghoop1(request):
    return render(request,'1_wed_hoop.html')

def weddinghoop2(request):
    return render(request,'2_wed_hoop.html')

def birthdayhoop(request):
    return render(request,'birthdayhoop.html')

def birthdayhoop1(request):
    return render(request,'1_birthday_hoop.html')

def birthdayhoop2(request):
    return render(request,'2_birthday_hoop.html')