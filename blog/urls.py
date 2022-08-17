from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog,name='blog'),
    path('<slug:category_slug>/<int:blog_id>',views.blog_detail,name='blog_detail'),
    path('categories/<slug:category_slug>', views.category_detail, name="courses_by_category"),
    path('tags/<slug:tag_slug>', views.tag_list, name="courses_by_tag"),
    
    
]
