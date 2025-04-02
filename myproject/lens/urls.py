from django .urls import path
from .views.auth_views import renderRegisterForm,renderLoginForm
from .views.home_views import renderDashboard
from .views.home_views import renderItem as render



urlpatterns = [
    path('register',renderRegisterForm),
    path('login',renderLoginForm),
    path('dashboard',renderDashboard),
    path('item',render),   

]
