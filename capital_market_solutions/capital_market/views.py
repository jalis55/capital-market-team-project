from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request,"index.html")

def teammembers(request):
    teammembers=TeamMembers.objects.all()
    context={
        "teammembers":teammembers
    }
    return render(request,'team.html',context)



def bc_clients(request):
    pass

def capita_clients(request):
    pass