from django.conf.urls import url
from django.urls import path, include
from .views import UserLoginView

urlpatterns = [
  path('api/login', UserLoginView.as_view()),
]