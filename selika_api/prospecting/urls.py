from django.urls import path
from .views.negociator_actions import ListNegociatorAPIView, GetNegociatorAPIView, UpdateNegociatorAPIView, \
    DeleteNegociatorAPIView, CreateNegociatorAPIView
from .views.crud_map import ListMapAPIView, GetMapAPIView, UpdateMapAPIView, DeleteMapAPIView, CreateMapAPIView
from .views.crud_road import ListRoutesAPIView, GetRouteAPIView, UpdateRouteAPIView, DeleteRouteAPIView, \
    CreateRouteAPIView

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