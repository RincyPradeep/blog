from django.urls import path
from web import views


app_name = "web"

urlpatterns = [
    path('',views.index, name="index"),
    path("category/<int:pk>/",views.category,name="category"),
    path("search/",views.search,name="search"),
]
