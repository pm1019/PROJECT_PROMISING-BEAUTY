from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('SendContact',views.SendContact,name='SendContact'),
    path('blog',views.blog,name='blog'),
    path('blog-details',views.blogdetails,name='blog-details'),
    path('search',views.search,name="search")

]
