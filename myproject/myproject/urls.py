from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('lens/', include('lens.urls')),  # Include URLs from the 'lens' app
    path('cart/', include('cart.urls')),  # Include URLs from the 'cart' app
    path('accounts/', include('allauth.urls')),  # Include URLs for account management

    
]
