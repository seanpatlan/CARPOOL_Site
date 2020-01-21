from django.shortcuts import render
from .models import Ride
from django.utils import timezone


def home(request):
    context = {
        'waiting_list': Ride.objects.all().filter(waiting=True),
        'riding_list': Ride.objects.all().filter(riding=True),
        'done_list': Ride.objects.all().filter(done=True),
        'cancelled_list': Ride.objects.all().filter(cancelled=True),
        'deleted_list': Ride.objects.all().filter(deleted=True),
        'now': timezone.now(),
        'title': 'Phone List',
        'phone_list': 'active',
        'all': True,
    }
    return render(request, 'phonelist/home.html', context)


def waiting(request):
    context = {
        'waiting_list': Ride.objects.all().filter(waiting=True),
        'title': 'Phone List',
        'phone_list': 'active',
        'waiting': True,
    }
    return render(request, 'phonelist/home.html', context)


def riding(request):
    context = {
        'riding_list': Ride.objects.all().filter(riding=True),
        'title': 'Phone List',
        'phone_list': 'active',
        'riding': True,
    }
    return render(request, 'phonelist/home.html', context)


def done(request):
    context = {
        'done_list': Ride.objects.all().filter(done=True),
        'title': 'Phone List',
        'phone_list': 'active',
        'done': True,
    }
    return render(request, 'phonelist/home.html', context)


def cancelled(request):
    context = {
        'cancelled_list': Ride.objects.all().filter(cancelled=True),
        'title': 'Phone List',
        'phone_list': 'active',
        'cancelled': True,
    }
    return render(request, 'phonelist/home.html', context)


def deleted(request):
    context = {
        'deleted_list': Ride.objects.all().filter(deleted=True),
        'title': 'Phone List',
        'phone_list': 'active',
        'deleted': True,
    }
    return render(request, 'phonelist/home.html', context)


def add_ride(request):
    return render(request, 'phonelist/add_ride.html')

