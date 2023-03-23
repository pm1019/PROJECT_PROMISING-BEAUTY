from django.shortcuts import render,redirect
from PRODUCT.models import P_Details

# Create your views here.
def custom(request):
    return render(request,'customizationhome.html')

def hoops(request):
    return render(request,'hoop.html')

def mm(request):
    if request.method == 'POST':
        custom_colour=request.POST['color']
        Prods=P_Details.objects.filter(p_color=custom_colour)
        return render(request,'matchmaking.html',{'Prods':Prods})

    else:
        return render(request,'matchmaking.html') 

def mm_final(request):
    p_id=request.GET.get('PRD_ID')
    if p_id:
        Prods=P_Details.objects.filter(p_type='Kurti Set',p_color='Pink')
        Foots=P_Details.objects.filter(p_color='black', p_type='Footwear') 
        Data={
            'Foots': Foots,
            'Prods':Prods
        }
        return render(request,'matchmakingfinal.html' ,Data)
    else:
     return render(request,'matchmaking2.html',{'Prods':Prods}) 

def mm_kurti(request):
    Prods=P_Details.objects.filter(p_type='Kurti Set')
    return render(request,'matchmaking2.html',{'Prods':Prods}) 

def mm_dress(request):
    return render(request,'matchmaking2.html')

def mm_lehenga(request):
    Prods=P_Details.objects.filter(p_type='Lehenga')
    return render(request,'matchmaking2.html',{'Prods':Prods}) 

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

def dress(request):
    return render(request,'product_customization.html')

def pearshape(request):
    if request.method == 'POST':
        custom_size=request.POST['size']
        custom_fabric=request.POST['fabric']
        custom_colour=request.POST['color']
    
        Prods=P_Details.objects.filter(p_fabric=custom_fabric,p_size=custom_size,p_color=custom_colour)
        return render(request,'pearshapefinal.html',{'Prods':Prods})

    else:
        return render(request,'pear_shape_customization_form.html')    



def invertedshape(request):
    return render(request,'inverted_triangle_shape_customization_form.html')

def appleshape(request):
    return render(request,'apple_shape_customization_form.html')

def rectangleshape(request):
    return render(request,'rectangle_shape_customization_form.html')

def hourglassshape(request):
    return render(request,'hourglass_shape_customization_form.html')
