from django.urls import path

from .views import CreateUpdateDestroyComments, ListDetailPosts, ListPosts

urlpatterns = [
    path('<int:pk>', ListDetailPosts.as_view(), name='open_post'),
    path('', ListPosts.as_view(), name='print_posts'),
    path('comment/', CreateUpdateDestroyComments.as_view(), name='comment')
]
