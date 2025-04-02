
from django.shortcuts import render

def renderDashboard(request):
    return render(request, 'auth/dashboard.html')

def renderItem(request):
    return render(request, 'auth/item.html')