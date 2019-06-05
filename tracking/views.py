from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect (index)

        else:
            # Return an 'invalid login' error message.
            return render(request, 'registration/login.html', {
                'error_msg': 'Invalid Credentials!'
            })

    else:
        return render(request, 'registration/login.html')

def logout_view(request):
    logout(request) 
    return redirect(login_view)

def register(request):

    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        search_username = User.objects.filter(username=username).exists()
        search_email = User.objects.filter(email=email).exists()

        email_error = False
        username_error = False

        if search_email or search_email:

            if search_email:
                email_error = True
            if search_username:
                username_error = True
        
            return render(request, 'registration/register.html', {
                "email_error": email_error,
                "username_error": username_error
            })
        else:
            User.objects.create_user(username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password)

            #success, the user doesn't already exist

            return redirect(reg_success)
    else:
        
        return render (request, 'registration/register.html')

def reg_success(request):

    return render(request, 'registration/success.html')

@login_required
def index(request):

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'application/index.html')
