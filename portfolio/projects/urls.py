from django.urls import path
from .views import projects, project_detail

urlpatterns = [
    path("", projects, name="projects"),
    path('<int:project_id>', project_detail, name=('detail'))
]