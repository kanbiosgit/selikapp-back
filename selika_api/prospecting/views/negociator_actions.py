from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Negociator, Route, Map
from ..serializers.income import MapIncomeSerializer, NegociatorIncomeSerializer, RouteIncomeSerializer
from userprofile.models import UserCustomGroup
from user.models import AAUser

class ListNegociatorAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Negociator.objects.all()
    serializer_class = NegociatorIncomeSerializer


class GetNegociatorAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Negociator.objects.all()
    serializer_class = NegociatorIncomeSerializer


class UpdateNegociatorAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Negociator.objects.all()
    serializer_class = NegociatorIncomeSerializer


class DeleteNegociatorAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Negociator.objects.all()
    serializer_class = NegociatorIncomeSerializer


class CreateNegociatorAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Negociator.objects.all()
    serializer_class = NegociatorIncomeSerializer

    def create(self, request):
        try :
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = AAUser.objects.get(id=request.user.id)
            userCust = UserCustomGroup.objects.create(label="negociator")
            negociator = Negociator.objects.create(user=user, custom_group=userCust, color=serializer.data['color'], lastname=serializer.data['lastname'], firstname=serializer.data['firstname'])
            statusCode = 200
            response = {
                'success': True,
                'id': str(negociator.id)
            }
        except Exception as e :
            statusCode = 400
            response = {
                'success': False,
                'statusCode': statusCode,
                'message': 'User does not exists',
                'error': str(e)
            }
        return Response(response, status=statusCode)