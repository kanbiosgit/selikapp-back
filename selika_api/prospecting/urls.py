from django.urls import path
from .views.negociator_actions import NegociatorList, NegociatorDetail
from .views.crud_map import ListMapAPIView, GetMapAPIView, UpdateMapAPIView, DeleteMapAPIView, CreateMapAPIView
from .views.crud_road import RouteDetail, RouteList, RouteFromMapDetail, RouteFromMapList

urlpatterns = [
    path('negociator', NegociatorList.as_view()),
    path('negociator/<int:pk>', NegociatorDetail.as_view()),
    path('route/<int:pk>', RouteDetail.as_view()),
    path('route/', RouteList.as_view()),
    path('map/route', RouteFromMapList.as_view()),
    path('map/route/<int:pk>', RouteFromMapDetail.as_view()),
    path('map/detail', ListMapAPIView.as_view()),
    path('map/<int:pk>/detail', GetMapAPIView.as_view()),
    path('map/<int:pk>/delete', DeleteMapAPIView.as_view()),
    path('map/<int:pk>/update', UpdateMapAPIView.as_view()),
    path('map/create', CreateMapAPIView.as_view()),
]