from django.urls import path

from .views import CreateMessageAPI

urlpatterns = [
    path('', CreateMessageAPI.as_view())
]
