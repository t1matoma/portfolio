from django.shortcuts import render
from .models import Projects


# Create your views here.

def projects(request):
    context = {'projects': Projects.objects.all()}
    return render(request, 'projects/projects.html', context)

def project_detail(request, project_id):
    details = Projects.objects.get(id=project_id)
    return render(request,'projects/detail.html', {'details': details})
