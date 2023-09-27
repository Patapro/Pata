from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from dashboard.dashapi.serializer import ServiceProviderPesrsonalInfoSerializer, ServiceProviderWorkInfoSerializer
from dashboard.models import ServiceProviderPersonalInfo, ServiceProviderWorkInfo
class ServiceProviderPersonalInfoAV(APIView):
    
    def post(self, request):
        serializer = ServiceProviderPesrsonalInfoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
        
    def put(self, request, pk):
        try:
            personal_info = ServiceProviderPersonalInfo.objects.get(pk = pk)
        except ServiceProviderPersonalInfo.DoesNotExist: 
            return Response({'Error' : 'INFO NOT FOUND'}, status=status.HTTP_404_NOT_FOUND) 
          
        serializer = ServiceProviderPesrsonalInfoSerializer(personal_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ServiceProviderWorkInfoAV(APIView):
    
    def post(self, request):
        serializer = ServiceProviderWorkInfoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
        
    def put(self, request, pk):
        try:
            personal_info = ServiceProviderWorkInfo.objects.get(pk = pk)
        except ServiceProviderWorkInfo.DoesNotExist: 
            return Response({'Error' : 'INFO NOT FOUND'}, status=status.HTTP_404_NOT_FOUND) 
          
        serializer = ServiceProviderWorkInfoSerializer(personal_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        