from django.urls import path
from .views import print_posts
urlpatterns = [
    path('', print_posts, name = 'print_posts')
]