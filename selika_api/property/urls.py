from django.urls import path
from .views import PropertyList, PropertyDetail, AdminPropertySearch, PropertyListProspecting

urlpatterns = [
    path('property', PropertyList.as_view()),
    path('property/<int:pk>', PropertyDetail.as_view()),
    path('admin/property', AdminPropertySearch.as_view()),
    path('property/prospecting', PropertyListProspecting.as_view())
]
