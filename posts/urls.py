from django.urls import path
from posts import views


app_name = "posts"

urlpatterns = [
    path("singlepost/<int:pk>/",views.singlepost,name="singlepost"),
    path("myposts/<int:pk>/",views.myposts,name="myposts"),
    path("create-post/",views.createpost,name="create-post"),
    path("update-post/<int:pk>/",views.updatepost,name="update-post"),
    path("delete-post/<int:pk>/",views.deletepost,name="delete-post"),
]
