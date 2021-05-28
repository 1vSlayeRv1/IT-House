from django.urls import path

from .views import RegisterView, LoginView
urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('signin/', LoginView.as_view())
]