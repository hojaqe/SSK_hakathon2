from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Аккаунт успешно создан', status=200)
    

# class ActivationView(APIView):
#      def post(self, request):
#         serializer = ActivationSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.activate() 
#         return Response('Аккаунт успешно активирован', status=200)
