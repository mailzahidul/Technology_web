from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.contrib import messages
from blog.models import Category, Tags
# Create your views here.



def projects(request):
    context = {}

    context['recent_projects']= Project.objects.filter(active=True).order_by('-create_date')[:3]
    context['project_categories']= Category.objects.filter(active=True).annotate(num_projects=Count('project')).order_by('-num_projects')
    context['project_tags']= Tags.objects.all()


    project_list=Project.objects.filter(is_published=True, active=True)

    
    paginator = Paginator(project_list, 3)
    page = request.GET.get('page',1)
    try:
        projects = paginator.page(page)
    except:
        projects = paginator.page(paginator.num_pages)
    
    context['projects']=projects
    return render(request, 'projects.html', context)



def project_details(request, slug):
    context = {}
    context['single_project']=Project.objects.get(is_published=True, active=True, slug=slug)

    context['recent_projects']= Project.objects.filter(active=True).order_by('-create_date')[:3]
    context['project_categories']= Category.objects.filter(active=True).annotate(num_projects=Count('project')).order_by('-num_projects')
    context['project_tags']= Tags.objects.all()
    return render(request, 'project-details.html', context)




def search_project_data(request):
    context = {}
    context['recent_projects']= Project.objects.filter(active=True).order_by('-create_date')[:2]
    context['project_categories']= Category.objects.filter(active=True).annotate(num_projects=Count('project')).order_by('-num_projects')
    context['project_tags']= Tags.objects.all()

    project_list=Project.objects.filter(is_published=True, active=True).all()
    search = request.GET.get('keyword')
    if search is not None:
        projects = project_list.filter(
        Q(title__icontains=search) | 
        Q(short_description__icontains=search) | 
        Q(description__icontains=search) | 
        Q(category__name__icontains=search) | 
        Q(tags__name__icontains=search)
        ).distinct()
        
        if projects.exists():
            context['projects'] = projects
            return render(request, 'projects.html', context)
        else:
            messages.error(request, "There is no similar content here..", extra_tags='alert-danger')
            context['projects']=project_list
    return render(request, 'projects.html', context)




def projects_search_by_category(request, id):
    context={}
    project_list= Project.objects.filter(active=True, category=id)
    context['recent_projects']= Project.objects.filter(active=True).order_by('-create_date')[:3]
    context['project_categories']= Category.objects.filter(active=True).annotate(num_projects=Count('project')).order_by('-num_projects')
    context['project_tags']= Tags.objects.all()

    paginator = Paginator(project_list, 3)
    page = request.GET.get('page',1)
    try:
        projects = paginator.page(page)
    except:
        projects = paginator.page(paginator.num_pages)

    if projects:
        context['projects']=projects
    else:
        messages.error(request, "There is no similar content here..", extra_tags='alert-danger')
        context['projects']=project_list
    return render(request, 'projects.html', context)


def project_search_by_tag(request, id):
    context={}
    project_list= Project.objects.filter(active=True, tags=id)
    # search_list = blog_list.filter(tags=id)

    context['recent_projects']= Project.objects.filter(active=True).order_by('-create_date')[:3]
    context['project_categories']= Category.objects.filter(active=True).annotate(num_projects=Count('project')).order_by('-num_projects')
    context['project_tags']= Tags.objects.all()

    paginator = Paginator(project_list, 3)
    page = request.GET.get('page',1)
    try:
        projects = paginator.page(page)
    except:
        projects = paginator.page(paginator.num_pages)

    if projects:
        context['projects']=projects
    else:
        messages.error(request, "There is no similar content here..", extra_tags='alert-danger')
        context['projects']=project_list
    return render(request, 'projects.html', context)