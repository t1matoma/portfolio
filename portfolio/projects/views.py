from django.shortcuts import render
from .models import Projects


# Create your views here.

import re
from django.shortcuts import render
from .models import Projects

def extract_video_id(url):
    """
    Извлекает ID видео из YouTube URL.
    """
    match = re.search(r'(https?://(?:www\.)?youtube\.com/watch\?v=|https?://youtu\.be/)([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(2)
    return None

def project_detail(request, project_id):
    details = Projects.objects.get(id=project_id)
    
    # Извлечь ID видео из URL, если он есть
    video_id = extract_video_id(details.video_url) if details.video_url else None

    return render(request, 'projects/detail.html', {'details': details, 'video_id': video_id})


def projects(request):
    context = {'projects': Projects.objects.all()}
    return render(request, 'projects/projects.html', context)

def project_detail(request, project_id):
    details = Projects.objects.get(id=project_id)
    
    video_id = extract_video_id(details.video_url) if details.video_url else None

    return render(request, 'projects/detail.html', {'details': details, 'video_id': video_id})

