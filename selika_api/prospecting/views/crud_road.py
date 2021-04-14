from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Route
from ..serializers.income import RouteIncomeSerializer

class ListRoutesAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Route.objects.all()
    serializer_class = RouteIncomeSerializer


class GetRouteAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Route.objects.all()
    serializer_class = RouteIncomeSerializer


class UpdateRouteAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Route.objects.all()
    serializer_class = RouteIncomeSerializer


class DeleteRouteAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Route.objects.all()
    serializer_class = RouteIncomeSerializer


class CreateRouteAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Route.objects.all()
    serializer_class = RouteIncomeSerializer