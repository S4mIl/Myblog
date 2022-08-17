from django.shortcuts import render
from .models import Tag,Category,Blog
# Create your views here.

def blog(request):
    blog=Blog.objects.all()
    tags=Tag.objects.all()
    category=Category.objects.all()
    randomproducts=Blog.objects.all().order_by('?')[:4]
    context={
        'blog':blog,
        'tags':tags,
        'category':category,
        'randomproducts':randomproducts,
    }
    return render(request,'blog/blog.html',context)
def blog_detail(request,category_slug,blog_id):
    randomproducts=Blog.objects.all().order_by('?')[:4]
    blog=Blog.objects.get(category__slug=category_slug,id=blog_id)
    category=Category.objects.all()
    tags=Tag.objects.all()
    context={
        'blog':blog,
        'tags':tags,
        'category':category,
        'randomproducts':randomproducts,
        
    } 
    return render(request,'blog/blog_detail.html',context)

def category_detail(request,category_slug):
    blog=Blog.objects.all().filter(category__slug=category_slug)
    category=Category.objects.all()
    tags=Tag.objects.all()
    
   
    context={
        'blog':blog,
        'category':category,
        'tags':tags,
        
    } 
    return render(request,'blog/blog.html',context)
def tag_list(request,tag_slug):
    blog=Blog.objects.all().filter(tags__slug=tag_slug)
    category=Category.objects.all()
    tags=Tag.objects.all()
    
    context={
        'blog':blog,
        'category':category,
        'tags':tags,
        
        
    } 
    return render(request,'blog/blog.html',context)
