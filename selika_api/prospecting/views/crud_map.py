from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Negociator, Route, Map
from .serializers.income import MapIncomeSerializer, NegociatorIncomeSerializer, RouteIncomeSerializer
from userprofile.models import UserCustomGroup
from user.models import AAUser

class ListMapAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Map.objects.all()
    serializer_class = MapIncomeSerializer


class GetMapAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Map.objects.all()
    serializer_class = MapIncomeSerializer


class UpdateMapAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Map.objects.all()
    serializer_class = MapIncomeSerializer


class DeleteMapAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Map.objects.all()
    serializer_class = MapIncomeSerializer


class CreateMapAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Map.objects.all()
    serializer_class = MapIncomeSerializer