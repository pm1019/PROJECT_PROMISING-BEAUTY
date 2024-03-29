from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('custom',views.custom,name="custom"),
    path('hoops',views.hoops,name="hoops"),
    path('mm',views.mm,name="mm"),
    path('mm_final',views.mm_final,name="mm_final"),
    path('mm_kurti',views.mm_kurti,name="mm_kurti"),
    path('mm_dress',views.mm_dress,name="mm_dress"),
    path('mm_lehenga',views.mm_lehenga,name="mm_lehenga"),
    path('bestperson',views.bestperson,name="bestperson"),
    path('bestperson1',views.bestperson1,name="bestperson1"),
    path('bestperson2',views.bestperson2,name="bestperson2"),
    path('namehoop',views.namehoop,name="namehoop"),
    path('namehoop1',views.namehoop1,name="namehoop1"),
    path('namehoop2',views.namehoop2,name="namehoop2"),
    path('weddinghoop',views.weddinghoop,name="weddinghoop"),
    path('weddinghoop1',views.weddinghoop1,name="weddinghoop1"),
    path('weddinghoop2',views.weddinghoop2,name="weddinghoop2"),
    path('birthdayhoop',views.birthdayhoop,name="birthdayhoop"),
    path('birthdayhoop1',views.birthdayhoop1,name="birthdayhoop1"),
    path('birthdayhoop2',views.birthdayhoop2,name="birthdayhoop2"),
    path('dress',views.dress,name="dress"),
    path('pearshape',views.pearshape,name="pearshape"),
    path('invertedshape',views.invertedshape,name="invertedshape"),
    path('appleshape',views.appleshape,name="appleshape"),
    path('rectangleshape',views.rectangleshape,name="rectangleshape"),
    path('hourglassshape',views.hourglassshape,name="hourglassshape")
]