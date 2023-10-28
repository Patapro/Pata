from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from dashboard.dashapi.serializer import ServiceProviderPesrsonalInfoSerializer, ServiceProviderWorkInfoSerializer, RequestServiceSerializer, ClientInfoSerializer
from dashboard.models import ServiceProviderPersonalInfo, ServiceProviderWorkInfo, ServiceRequest, ClientInfo

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
    
class AdminServiceProviderApproval(APIView):
    def get(self, request):
        pending_requests = ServiceProviderWorkInfo.objects.filter(status="Pending")
        serializer = ServiceProviderWorkInfoSerializer(pending_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ApproveRequest(APIView):
    def post(self, request, pk):
        try:
            request = ServiceProviderWorkInfo.objects.get(pk=pk)
            request.status = "Approved"
            request.save()
            return Response({"detail": "Request approved."})
        except ServiceProviderWorkInfo.DoesNotExist:
            return Response({"detail": "Request not found."}, status=404)

class RejectRequest(APIView):
    def post(self, request, pk):
        try:
            request = ServiceProviderWorkInfo.objects.get(pk=pk)
            request.status = "Rejected"
            request.save()
            return Response({"detail": "Request rejected."})
        except ServiceProviderWorkInfo.DoesNotExist:
            return Response({"detail": "Request not found."}, status=404)

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
        
class ServiceProvierRequestApprove(APIView):
    
    def post(self, request, pk):
        try:
            personal_info = ServiceProviderWorkInfo.objects.get(pk=pk)
            personal_info.status = "Pending"  # Update the status to indicate a request for approval
            personal_info.save()
            
            serializer = ServiceProviderWorkInfoSerializer(personal_info)
            return Response(serializer.data)
        except ServiceProviderWorkInfo.DoesNotExist:
            return Response({"detail": "Service provider information not found."}, status=404)

    
class ServiveProviderRequestInfo(APIView):
    
    def get(self, request, client_id):
        try:
            client_info = ClientInfo.objects.get(pk=client_id)
            request = ServiceRequest.objects.get(client=client_info)
            serializer = ServiceProviderWorkInfoSerializer(client_info, many=True)
            return Response(serializer.data)
        except ClientInfo.DoesNotExist:
            return Response({'Error' : 'INFO NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)
        
class LandingPage(APIView):
    
    def get(self,request):
        personal_info = ServiceProviderWorkInfo.objects.filter(status = "Approved").all()
        serializer = ServiceProviderWorkInfoSerializer(personal_info, many=True)
        return Response(serializer.data)
class LandingPageServiceProviderSF(generics.ListAPIView):
    serializer_class = ServiceProviderWorkInfoSerializer  

    def get_queryset(self):
        service_query = self.request.query_params.get('service', None)
        location_query = self.request.query_params.get('location', None)

        queryset = ServiceProviderWorkInfo.objects.all()

        if service_query:
            queryset = queryset.filter(profession__icontains=service_query)

        if location_query:
            queryset = queryset.filter(location__icontains=location_query)
        return queryset

class AdmindashboardServiceProviderSF(generics.ListAPIView):
    serializer_class = ServiceProviderWorkInfoSerializer  

    def get_queryset(self):
        service_query = self.request.query_params.get('service', None)

        queryset = ServiceProviderWorkInfo.objects.all()

        if service_query:
            queryset = queryset.filter(profession__icontains=service_query)

        return queryset
    
class RequestService(APIView):
    
    def post(self, request):
        serializer = RequestServiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ServiceProvidersAnalytics(APIView):
    def get(self, request):
        service_providers_count = ServiceProviderWorkInfo.objects.count()

        response_data = {
            "Number of service providers": service_providers_count,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
class PendingRequestAnalytics(APIView):
    def get(self, request):
        pending_requests = ServiceProviderWorkInfo.objects.filter(status="Pending").count()

        response_data = {
            "Total request": pending_requests,
        }
        return Response(response_data, status=status.HTTP_200_OK)