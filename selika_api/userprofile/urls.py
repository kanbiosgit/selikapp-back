from django.urls import path
from .views import UserProfileList, UserProfileDetail, SelfUserProfile

urlpatterns = [
    path('userprofile', UserProfileList.as_view()),
    path('userprofile/<int:pk>', UserProfileDetail.as_view()),
    path('userprofile/me', SelfUserProfile.as_view())
]