from django.urls import path,URLPattern
from . import views

urlpatterns = [
   path('bag',views.bag,name="bag"),
    path('proceed_checkout',views.proceed_checkout,name="proceed_checkout")
]