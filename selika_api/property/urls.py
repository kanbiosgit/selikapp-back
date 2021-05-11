from django.urls import path
from .views import PropertyList, PropertyDetail, AdminPropertySearch, PropertyListProspecting, PropertyFromNegociator, CommentOnProperty, CommentDetail

urlpatterns = [
    path('property', PropertyList.as_view()),
    path('property/<int:pk>', PropertyDetail.as_view()),
    path('admin/property', AdminPropertySearch.as_view()),
    path('property/prospecting', PropertyListProspecting.as_view()),
    path('property/negociator/prospecting', PropertyFromNegociator.as_view()),
    path('property/<int:pk>/comment', CommentOnProperty.as_view()),
    path('comment/<int:pk>', CommentDetail.as_view())
]
