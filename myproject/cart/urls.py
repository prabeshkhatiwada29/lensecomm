from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart, product_list

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('products/', product_list, name='product_list'),
]