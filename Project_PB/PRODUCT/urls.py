from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('product',views.product,name="shop"),
    path('add-to-wishlist/<int:id>',views.addToWishlist,name='add-to-wishlist'),
    path('show_wishlist',views.show_wish,name='show_wishlist'),
    path('add-to-bag/<int:id>',views.addTobag,name='add-to-bag'),
    path('show_bag',views.show_bag,name='show_bag'),
    path('remove_wish/<int:id>',views.remove_wish,name='remove_wish'),
    path('remove_bag/<int:id>',views.remove_bag,name='remove_bag'),
    path('product-detail/<int:id>',views.prod_detail,name='product-detail'),
    path('search',views.search,name="search"),
    path('low_to_high',views.low_to_high,name='low_to_high'),
    path('high_to_low',views.high_to_low,name='high_to_low'),
    path('categories',views.categories,name="categories"),
    path('bags',views.bags,name="bags")
]
