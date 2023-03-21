from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('set_pass',views.set_pass,name="set_pass")
]