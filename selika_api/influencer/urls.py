from .views import InfluencerDetail, InfluencerList
from django.urls import path

urlpatterns = [
    path('influencer', InfluencerList.as_view()),
    path('influencer/<int:pk>', InfluencerDetail.as_view())
]