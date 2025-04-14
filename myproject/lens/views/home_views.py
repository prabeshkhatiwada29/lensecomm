
from django.shortcuts import render


def renderItem(request):
    return render(request, 'auth/item.html')

def renderlanding(request):
    return render(request, 'auth/landingpage.html')
