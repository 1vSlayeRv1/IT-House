from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegisterView

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('signin/', obtain_jwt_token)
]
