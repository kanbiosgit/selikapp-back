from django.conf.urls import url
from django.urls import path, include
from .views import UserLoginView, RetrieveUser

urlpatterns = [
  path('api/login', UserLoginView.as_view()),
  path('api/current', RetrieveUser.as_view())
]