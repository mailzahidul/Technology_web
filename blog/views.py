from django.shortcuts import render
from .models import Blog, Category, Tags
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def blogs(request):
    context = {}
    blog_list= Blog.objects.filter(active=True).all()
    
    paginator = Paginator(blog_list, 9)
    page = request.GET.get('page',1)
    try:
        blogs = paginator.page(page)
    except:
        blogs = paginator.page(paginator.num_pages)
    
    context['blogs']=blogs
    return render(request, 'blog.html', context)


def blog_details(request, slug):
    context = {}
    single_blog = Blog.objects.get(active=True, slug=slug)
    context['blog_details'] = single_blog
    context['recent_post']= Blog.objects.filter(active=True).order_by('-create_date')[:5]
    context['related_post']= Blog.objects.filter(active=True, category=single_blog.category).exclude(slug=slug).order_by('-create_date')[:5]
    context['categories']= Category.objects.filter(active=True).annotate(num_posts=Count('blog')).order_by('-num_posts')
    context['tags']= Tags.objects.all()
    return render(request, 'blog-details.html', context)



def category_search(request, id):
    context={}
    blog_list= Blog.objects.filter(active=True)
    search_list = blog_list.filter(category=id)

    paginator = Paginator(search_list, 9)
    page = request.GET.get('page',1)
    try:
        blogs = paginator.page(page)
    except:
        blogs = paginator.page(paginator.num_pages)

    if blogs:
        context['blogs']=blogs
    else:
        messages.error(request, "There is no similar post here..", extra_tags='alert-danger')
        context['blogs']=blog_list
    return render(request, 'blog.html', context)


def tag_search(request, id):
    context={}
    blog_list= Blog.objects.filter(active=True)
    search_list = blog_list.filter(tags=id)

    paginator = Paginator(search_list, 9)
    page = request.GET.get('page',1)
    try:
        blogs = paginator.page(page)
    except:
        blogs = paginator.page(paginator.num_pages)

    if blogs:
        context['blogs']=blogs
    else:
        messages.error(request, "There is no similar post here..", extra_tags='alert-danger')
        context['blogs']=blog_list
    return render(request, 'blog.html', context)



def search_data(request):
    context = {}
    blog_list= Blog.objects.filter(active=True).all()
    search = request.GET.get('keyword')
    if search is not None:
        posts = blog_list.filter(
        Q(title__icontains=search) | 
        Q(sort_description__icontains=search) | 
        Q(description__icontains=search) | 
        Q(category__name__icontains=search) | 
        Q(tags__name__icontains=search)
        ).distinct()

        if posts.exists():
            context['blogs'] = posts
            return render(request, 'blog.html', context)
        else:
            messages.error(request, "There is no similar post here..", extra_tags='alert-danger')
    return render(request, 'blog.html', context)


    
# def search_data(request):
#     context = {}

#     blog_list= Blog.objects.filter(active=True).all()
#     search = request.GET.get('keyword')
#     if search is not None:
#         posts = blog_list.filter(
#         Q(title__icontains=search) | 
#         Q(sort_description__icontains=search) | 
#         Q(description__icontains=search) | 
#         Q(category__name__icontains=search) | 
#         Q(tags__name__icontains=search)
#         ).distinct()

#         if posts.exists():
#             paginator = Paginator(posts, 4)
#             page = request.GET.get('page',1)
#             try:
#                 blogs = paginator.page(page)
#             except:
#                 blogs = paginator.page(paginator.num_pages)

#             context['blogs'] = blogs
#             return render(request, 'blog.html', context)
#         else:
#             messages.error(request, "There is no similar post here..", extra_tags='alert-danger')

#     context['blogs']=blogs
#     return render(request, 'blog.html', ccontext)