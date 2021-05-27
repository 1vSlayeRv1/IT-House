from django.urls import path
from .views import print_posts, open_post
urlpatterns = [
    path('<int:post_id>', open_post, name='open_post'),
    path('', print_posts, name='print_posts')
]
