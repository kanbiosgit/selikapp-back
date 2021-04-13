from django.urls import path
from .views import ListPropertiesAPIView, GetPropertyAPIView, DeletePropertyAPIView, CreatePropertyAPIView, UpdatePropertyAPIView

urlpatterns = [
    path('property', ListPropertiesAPIView.as_view()),
    path('property/<int:pk>/detail', GetPropertyAPIView.as_view()),
    path('property/create', CreatePropertyAPIView.as_view()),
    path('property/<int:pk>/update', UpdatePropertyAPIView.as_view()),
    path('property/<int:pk>/delete', DeletePropertyAPIView.as_view()),
]
