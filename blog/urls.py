from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<slug:slug>/', views.blog_details, name="blog-details"),
    path('search/', views.search_data, name="search_data"),
    path('category_search/<int:id>', views.category_search, name="category_search"),
    path('tag_search/<int:id>', views.tag_search, name="tag_search")

]