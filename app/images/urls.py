from django.urls import path
from .views import ProfileFileUploadView

urlpatterns = [
    path('upload/', ProfileFileUploadView.as_view(), name='images')

]