from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework import generics

from awards.forms import UserUpdateForm, ProfileUpdateForm,  UserRegisterForm, RateForm,ProjectUploadForm
from awards.models import Project,User,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    '''
    View function that renders home
    '''
    projects = Project.objects.all()
    users = User.objects.all()

    return render(request, 'home.html', {"projects":projects, "users": users})


def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'project.html', {'project': project})

class ListProjectView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"projects": searched_projects})
    else:
        message = "You haven't searched for any projects yet"
    return render(request, 'search.html', {'message': message})

@login_required
def profile(request):
    projects = request.user.profile.projects.all()
    return render(request, 'profile.html', {"projects":projects})

class ListProfileView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



@login_required
def update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your account!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update.html', context)


@login_required
def upload_project(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.save()
            messages.success(request, f'Successfully uploaded your Project!')
            return redirect('home')
    else:
        form = ProjectUploadForm()
    return render(request, 'upload_project.html', {"form": form, "users": users})
    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})
    
@login_required
def rate(request, project_id):
    project = Project.objects.get(id=project_id)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.project = project
            rate.save()
        return render(request, 'project.html', locals())
    else:
        form = RateForm()
    return render(request, 'rate.html', locals())

