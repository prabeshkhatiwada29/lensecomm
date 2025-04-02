
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def renderRegisterForm(request):
    if request.method == 'POST':
        # Handle form submission here
        # For example, you can save the user data to the database
     username=request.POST['username']
     email=request.POST['email']
     password=request.POST['password']
     
     user=User.objects.create(
        username=username,
        email=email,
        )
     user.set_password(password)
     user.save()
     
     return redirect('/lens/login')
           
    
    else:
        # Render the registration form
       
        return render(request, 'auth/register.html')
def renderLoginForm(request):
    if request.method == 'POST':
       email=request.POST['email']
       password=request.POST['password']
       user = authenticate(request, username=email, password=password)
       if user is not None:
          login(request, user)
          return redirect('/lens/item.html')
       else:
            messages.error(request, 'Invalid email or password')
            return redirect('/lens/login')
          
    return render(request, 'auth/login.html')