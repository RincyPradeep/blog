from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from web.models import Post,Category,User


def index(request):
    posts = Post.objects.filter(is_deleted = False)
    categories = Category.objects.all()

    context = {
        "posts" : posts,
        "categories" : categories
    }
    return render(request,"web/index.html",context=context)

def category(request,pk):
    posts = Post.objects.filter(is_deleted = False)
    posts = posts.filter(category_id = pk)
    categories = Category.objects.all()
    context = {
        "posts" : posts,
        "categories" : categories
    }
    return render(request,"web/index.html", context = context)
   
def search(request):   
    posts = Post.objects.filter(is_deleted = False)
    categories = Category.objects.all()
    q = request.GET.get("query")
    if q:
        posts = posts.filter(Q(title__icontains = q) | (Q(description__icontains = q)))
    context={
        "posts" : posts,
        "categories" : categories
    }
    return render(request,"web/index.html", context = context)

