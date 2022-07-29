import json
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,reverse
from django.shortcuts import redirect, render,get_object_or_404
from django.http.response import HttpResponse

from web.models import Post,Category


def singlepost(request,pk):
    post = get_object_or_404(Post.objects.filter(pk=pk))
    context={
        "post" : post,
    }
    return render(request,"posts/singlepost.html",context=context)


def myposts(request,pk):
    if request.user.is_authenticated:
        posts = Post.objects.filter(is_deleted = False)
        posts = posts.filter(author_id = pk)
        categories = Category.objects.all()
        context = {
            "posts" : posts,
            "categories" : categories
        }
        return render(request,"posts/myposts.html",context=context)
    else:
        return HttpResponseRedirect(reverse("users:login"))
        

def createpost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            author = request.POST.get("author")
            category = request.POST.get("category")
            title = request.POST.get("title")
            description = request.POST.get("description")

            Post.objects.create( 
                author_id = author,        
                title = title,
                category_id = category,
                description = description
            )

            response_data = {
                "status" : "success",
                "title" : "Successfully added",
                "message" : "Your post is added"
            }
            
            return HttpResponse(json.dumps(response_data), content_type = "application/javascript")
        else:
            categories = Category.objects.all()
            return render(request,"posts/create_post.html",{"categories" : categories })
    else:
        return HttpResponseRedirect(reverse("users:login"))


def updatepost(request,pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            author = request.POST.get("author")
            category = request.POST.get("category")
            title = request.POST.get("title")
            description = request.POST.get("description")

            Post.objects.filter(id = pk).update( 
                author_id = author,        
                title = title,
                category_id = category,
                description = description
            )
            return HttpResponseRedirect(reverse("posts:myposts", kwargs={'pk':author}))
        else:
            posts = Post.objects.filter(is_deleted = False)
            post = get_object_or_404(posts.filter(id = pk))
            categories = Category.objects.all()
            context = {
                "post" : post,
                "categories" : categories
            }
            
            return render(request,"posts/update_post.html",context = context)
    else:
        return HttpResponseRedirect(reverse("users:login"))


def deletepost(request,pk):
    if request.user.is_authenticated:
        Post.objects.filter(id = pk).update( 
            is_deleted = True,        
        )   

        return HttpResponseRedirect(reverse("posts:myposts", kwargs={'pk':request.user.id}))
    else:
        return HttpResponseRedirect(reverse("users:login"))
