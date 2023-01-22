from django.shortcuts import render
from .models import Post,Category
# Create your views here.

def category(request,category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'category': category
    }
    return render(request, 'blog/category.html', context)

def blog(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'blog/blog.html',context)
