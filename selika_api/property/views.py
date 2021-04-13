from django.db.models import query
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Property
from .serializers.income import PropertyIncomeSerializer
from prospecting.models import Negociator


# Create your views here.

class ListPropertiesAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Property.objects.all()
    serializer_class = PropertyIncomeSerializer


class GetPropertyAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Property.objects.all()
    serializer_class = PropertyIncomeSerializer


class UpdatePropertyAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Property.objects.all()
    serializer_class = PropertyIncomeSerializer


class DeletePropertyAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Property.objects.all()
    serializer_class = PropertyIncomeSerializer


class CreatePropertyAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Property.objects.all()
    serializer_class = PropertyIncomeSerializer

    # def post(self, request):
    #     negociator = Negociator.objets.get(user=request.user)
    #     request.data.append(negociator.id)
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
