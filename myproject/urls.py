from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lens/', include('lens.urls')),  # Include the app's URLs with the 'lens/' prefix
]