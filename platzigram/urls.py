from django.urls import path
from .views import hello_world, hi

urlpatterns = [
    path('hello-world/', hello_world),
    path('hi/', hi)
]
