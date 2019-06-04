from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# Create your views here.

def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect (index)

        else:
            # Return an 'invalid login' error message.
            return render(request, 'registration/login.html', {
                'error_msg': 'Invalid Credentials!'
            })

    else:
        return render(request, 'registration/login.html')

def register(request):

    if request.method == 'POST':
        
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']


    else:
        
        return render (request, 'registration/register.html')

def index(request):
    return render(request, 'application/index.html')
