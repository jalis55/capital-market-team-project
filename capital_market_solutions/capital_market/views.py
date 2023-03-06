from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    return render(request, "index.html")


def teammembers(request):
    teammembers = TeamMembers.objects.all()
    context = {
        "teammembers": teammembers
    }
    return render(request, 'team.html', context)


def bc_clients(request):
    bluechip_clients = Clients.objects.filter(application__name='Bluechip')
    context = {
        "bluechip_clients": bluechip_clients
    }
    return render(request, 'bluechip.html', context)


def capita_clients(request):
    pass
