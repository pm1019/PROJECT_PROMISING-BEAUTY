from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dashboard',views.DASHBOARD,name="dash"),
    path('show_data',views.show,name="show_data"),
    path('profile_error',views.profile_error,name="profile_error"),
    path('order_error',views.order_error,name="order_error"),
    path('wish_error',views.wish_error,name="wish_error"),
    path('bag_error',views.bag_error,name="bag_error")
]