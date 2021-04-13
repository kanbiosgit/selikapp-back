from django.conf.urls import url
from django.urls import path, include
from .views import UserLoginView
from userprofile.views import UserProfileView

urlpatterns = [
  path('api/login', UserLoginView.as_view()),
  path('api/profile', UserProfileView.as_view())
]