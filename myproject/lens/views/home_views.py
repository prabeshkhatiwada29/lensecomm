from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def renderItem(request):
    return render(request, 'auth/item.html')

def renderlanding(request):
    return render(request, 'auth/landingpage.html')

def renderCheckout(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip']
        payment_method = request.POST['payment_method']

        # Print order details for debugging
        print(f"Order Details: {first_name}, {last_name}, {address}, {city}, {state}, {zip_code}, {payment_method}")

        # Redirect to a success page
        return redirect('/lens/order_success')  # Replace with the correct success page URL
    else:
        # Render the checkout form if the request is not POST
        return render(request, 'auth/checkout.html')

def renderorderSuccess(request):
    
    return render(request, 'auth/order_success.html')