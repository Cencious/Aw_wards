from django.shortcuts import render,redirect
from awards.models import Project, User



def home(request):
    '''
    View function that renders home
    '''
    projects = Project.objects.all()
    users = User.objects.all()

    return render(request, 'home.html')

