from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('custom',views.custom,name="custom"),
    path('hoops',views.hoops,name="hoops")
]