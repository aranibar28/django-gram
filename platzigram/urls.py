from django.urls import path
from .views import hello_world, sorted_integer, say_hi
from posts.views import list_posts

urlpatterns = [
    # /hello-world/
    path('hello-world/', hello_world), 
    # /num/?numbers=10,4,50,32,25
    path('num/', sorted_integer),
    # /hi/Gerson/24/
    path('hi/<str:name>/<int:age>/', say_hi),

    path('posts/', list_posts)
]
