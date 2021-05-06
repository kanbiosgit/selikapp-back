from django.conf.urls import url
from django.urls import path, include
from .views import UserLoginView, RetrieveUser, createNegociator, sendEmail

urlpatterns = [
  path('api/login', UserLoginView.as_view()),
  path('api/current', RetrieveUser.as_view()),
  path('api/create/negociator', createNegociator.as_view()),
  path('api/send/email', sendEmail.as_view())
]