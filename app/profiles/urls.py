from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import (ListCreateProfileAPI, ProfileAvatarUploadView,
                    ProfileRoleAPI, RegisterView)

urlpatterns = [
    path('profile/role/', ProfileRoleAPI.as_view()),
    path('profile/avatar/', ProfileAvatarUploadView.as_view()),
    path('profile/', ListCreateProfileAPI.as_view()),
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('auth/signin/', obtain_jwt_token, name='signin'),
    path('auth/token-refresh/', refresh_jwt_token),
]
