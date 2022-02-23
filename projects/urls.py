
from django.urls import path
from . import views

urlpatterns = [
path('', views.projects, name="projects"),
path('details/<slug:slug>', views.project_details, name="project-details"),
path('search_project_data', views.search_project_data, name="search_project_data"),

path('projects_search_by_category/<int:id>', views.projects_search_by_category, name="projects_search_by_category"),
path('project_search_by_tag/<int:id>', views.project_search_by_tag, name="project_search_by_tag")


]



    
