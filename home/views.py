from django.shortcuts import render

# Create your views here.
from home.models import Project

def home(request):
    home = Project.objects.all()

    context = {

        'home': home

    }
    #return render(request,'home.html',{})
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html', {})

"""
def details(request, pk):

    project = Project.objects.get(pk=pk)

    context = {

        'home': home

    }

    return render(request, 'details.html', context)
"""