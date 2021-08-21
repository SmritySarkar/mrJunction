from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# from .models import Register

# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Name is already Taken....!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail is already Taken....!')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                username=username, password=password, email=email)
                user.save()
                messages.info(request, 'User Info Added Successfully!')
                return redirect('login')

        else:
            messages.info(request, 'Password is not Matching....!')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials....')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
