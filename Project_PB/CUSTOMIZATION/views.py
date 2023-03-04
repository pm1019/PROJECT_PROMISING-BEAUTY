from django.shortcuts import render
from PRODUCT.models import P_Details

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
