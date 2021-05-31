from django.urls import path
from .views import ListPosts, ListDetailPosts
urlpatterns = [
    path('<int:pk>', ListDetailPosts.as_view(), name='open_post'),
    path('', ListPosts.as_view(), name='print_posts')
]
