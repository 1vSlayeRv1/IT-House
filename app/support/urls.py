from django.urls import path

from .views import support_to_message

urlpatterns = [
    path('', support_to_message, name='support_to_message')
]
