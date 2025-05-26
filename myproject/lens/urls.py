from django.urls import path
from .views.auth_views import renderRegisterForm, renderLoginForm
from .views.home_views import renderlanding
from .views.home_views import renderItem as render
from .views.home_views import renderCheckout, renderorderSuccess

urlpatterns = [
    path('register', renderRegisterForm),
    path('login', renderLoginForm),
    path('item', render),
    path('landingpage', renderlanding),
    path('checkout', renderCheckout,),
    path('order-success', renderorderSuccess),
]



