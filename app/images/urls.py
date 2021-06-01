from django.urls import path, re_path
from .views import ProfileFileUploadView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', ProfileFileUploadView.as_view(), name='images')

]