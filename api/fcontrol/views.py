from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from fcontrol.models import Institution
from .serializers import InstitutionListSerializer, SensorDataSerializer, LoginSerializer


class InstitutionListView(GenericAPIView):
    serializer_class = InstitutionListSerializer
    def get_queryset(self):
        queryset = Institution.objects.all()
        return queryset
    def get(self,request):
        queryset = self.get_queryset()
        print(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SensorDataView(GenericAPIView):
    serializer_class = SensorDataSerializer


    def post(self,request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail':True})

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        print(user)
        return Response({'detail':True})
