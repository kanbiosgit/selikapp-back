from django.urls import path
from .views import PropertyList, PropertyDetail

urlpatterns = [
    path('property', PropertyList.as_view()),
    path('property/<int:pk>', PropertyDetail.as_view()),
]
