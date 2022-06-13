from django.shortcuts import render,redirect
from awards.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404



def home(request):
    '''
    View function that renders home
    '''
    # projects = Project.objects.all()
    users = User.objects.all()

    return render(request, 'home.html')

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'project.html', {'project': project})