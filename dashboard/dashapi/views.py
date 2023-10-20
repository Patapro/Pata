from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from dashboard.dashapi.serializer import ServiceProviderPesrsonalInfoSerializer, ServiceProviderWorkInfoSerializer
from dashboard.models import ServiceProviderPersonalInfo, ServiceProviderWorkInfo
# from dashboard.dashapi.permissions import IsAdminOrReadOnly
# class ServiceProviderPersonalInfoAV(APIView):
#     # permission_classes=[IsAdminOrReadOnly]
    
#     def post(self, request):
#         serializer = ServiceProviderPesrsonalInfoSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 
        
#     def put(self, request, pk):
#         try:
#             personal_info = ServiceProviderPersonalInfo.objects.get(pk = pk)
#         except ServiceProviderPersonalInfo.DoesNotExist: 
#             return Response({'Error' : 'INFO NOT FOUND'}, status=status.HTTP_404_NOT_FOUND) 
          
#         serializer = ServiceProviderPesrsonalInfoSerializer(personal_info, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class ServiceProviderWorkInfoAV(APIView):
#     # permission_classes=[IsAdminOrReadOnly]
    
#     def post(self, request):
#         serializer = ServiceProviderWorkInfoSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 
        
#     def put(self, request, pk):
#         try:
#             personal_info = ServiceProviderWorkInfo.objects.get(pk = pk)
#         except ServiceProviderWorkInfo.DoesNotExist: 
#             return Response({'Error' : 'INFO NOT FOUND'}, status=status.HTTP_404_NOT_FOUND) 
          
#         serializer = ServiceProviderWorkInfoSerializer(personal_info, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDashBoard(APIView):
    
    def get(self,request):
        personal_info = ServiceProviderWorkInfo.objects.all()
        serializer = ServiceProviderWorkInfoSerializer(personal_info, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            provider = ServiceProviderWorkInfo.objects.get(id=pk)
            provider.status = not provider.status
            provider.save()
            return Response({'message': 'Status changed'})
        except ServiceProviderWorkInfo.DoesNotExist:
            return Response({'error': 'Provider not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            provider = ServiceProviderWorkInfo.objects.get(id=pk)
        except ServiceProviderWorkInfo.DoesNotExist:
            return Response({'Error' : 'INFO NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        provider.delete()
        return Response({'message': 'Provider deleted'})
        
class ServiceProviderDashBoard(APIView):
    
    def get(self,request):
        personal_info = ServiceProviderWorkInfo.objects.get(user=self.request.user)
        serializer = ServiceProviderWorkInfoSerializer(personal_info, many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        personal_info = ServiceProviderWorkInfo.objects.get(user=self.request.user)
        serializer = ServiceProviderWorkInfoSerializer(personal_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class LandingPage(APIView):
    
    def get(self,request):
        personal_info = ServiceProviderWorkInfo.objects.all()
        serializer = ServiceProviderWorkInfoSerializer(personal_info, many=True)
        return Response(serializer.data)
        


class ServiceProviderSF(generics.ListAPIView):
    serializer_class = ServiceProviderWorkInfoSerializer  # Use the serializer class

    def get_queryset(self):
        service_query = self.request.query_params.get('service', None)
        location_query = self.request.query_params.get('location', None)

        queryset = ServiceProviderWorkInfo.objects.all()

        if service_query:
            queryset = queryset.filter(profession__icontains=service_query)

        if location_query:
            queryset = queryset.filter(location__icontains=location_query)
        return queryset
