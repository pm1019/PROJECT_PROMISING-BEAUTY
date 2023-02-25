from django.urls import path,URLPattern
from . import views

urlpatterns = [
   path('bag',views.bag,name="bag")
]