from django.urls import path
from .views import ListMapAPIView, ListRoutesAPIView, ListNegociatorAPIView, GetMapAPIView, GetRouteAPIView, GetNegociatorAPIView, UpdateNegociatorAPIView, UpdateRouteAPIView, UpdateMapAPIView, DeleteNegociatorAPIView, DeleteRouteAPIView, DeleteMapAPIView, CreateNegociatorAPIView, CreateMapAPIView, CreateRouteAPIView

urlpatterns = [
    path('negociator/detail', ListNegociatorAPIView.as_view()),
    path('negociator/update', UpdateNegociatorAPIView.as_view()),
    path('negociator/<int:pk>/detail', GetNegociatorAPIView.as_view()),
    path('negociator/<int:pk>/delete', DeleteNegociatorAPIView.as_view()),
    path('negociator/create', CreateNegociatorAPIView.as_view()),
    path('route/<int:pk>/detail', GetRouteAPIView.as_view()),
    path('route/detail', ListRoutesAPIView.as_view()),
    path('route/<int:pk>', UpdateRouteAPIView.as_view()),
    path('route/<int:pk>/delete', DeleteRouteAPIView.as_view()),
    path('route/create', CreateRouteAPIView.as_view()),
    path('map/detail', ListMapAPIView.as_view()),
    path('map/<int:pk>/detail', GetMapAPIView.as_view()),
    path('map/<int:pk>/delete', DeleteMapAPIView.as_view()),
    path('map/<int:pk>/update', UpdateMapAPIView.as_view()),
    path('map/create', CreateMapAPIView.as_view()),
]