from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Book

# Create your views here.


def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')


def book(request):

    if request.method == 'POST':
        begin = request.POST['begin']
        destination = request.POST['destination']
        depart = request.POST['depart']
        back = request.POST['back']
        adult = request.POST['adult']
        children = request.POST['children']
        travelClass = request.POST['travelClass']

        booking = Book(begin=begin, destination=destination,
                       depart=depart, back=back, adult=adult, children=children, travelClass=travelClass)
        booking.save()
        messages.info(request, 'Your Ticket is booked Successfully !!')
        return redirect('/')

    else:
        return render(request, 'book.html')


def bookings(request):

    info = Book.objects.all()
    return render(request, 'bookings.html', {'info': info})
