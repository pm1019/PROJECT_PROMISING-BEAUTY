from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('product',views.product,name="shop"),
    path('<int:id>',views.prods_detail),
    path('add-to-wishlist/<int:id>',views.addToWishlist,name='add-to-wishlist'),
    path('show_wishlist',views.show_wish,name='show_wishlist'),
    path('add-to-bag/<int:id>',views.addTobag,name='add-to-bag'),
    path('show_bag',views.show_bag,name='show_bag')
]