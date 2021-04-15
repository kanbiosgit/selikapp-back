from django.urls import path
from .views import UserProfileList, UserProfileDetail

urlpatterns = [
    path('api/userprofile', UserProfileList.as_view()),
    path('api/userprofile/<int:pk>', UserProfileDetail.as_view())
]