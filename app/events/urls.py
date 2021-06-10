from django.urls import path

from .views import ListEventsAPI, RetrieveUpdateDestroyEventsAPI

urlpatterns = [
    path('', ListEventsAPI.as_view()),
    path('add/', RetrieveUpdateDestroyEventsAPI.as_view())

]
