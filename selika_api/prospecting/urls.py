from django.urls import path
from .views.negociator_actions import NegociatorList, NegociatorDetail, NegociatorHimself
from .views.crud_map import MapList, MapDetail
from .views.crud_road import RouteDetail, RouteList, RouteFromMapDetail, RouteFromMapList

urlpatterns = [
    path('negociator', NegociatorList.as_view()),
    path('negociator/<int:pk>', NegociatorDetail.as_view()),
    path('route/<int:pk>', RouteDetail.as_view()),
    path('route/', RouteList.as_view()),
    path('map/route', RouteFromMapList.as_view()),
    path('map/route/<int:pk>', RouteFromMapDetail.as_view()),
    path('map', MapList.as_view()),
    path('map/<int:pk>', MapDetail.as_view()),
    path('negociator/me', NegociatorHimself.as_view())
]