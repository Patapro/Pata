from rest_framework import serializers
from dashboard.models import ServiceProviderPersonalInfo, ServiceProviderWorkInfo, ServiceRequest, ClientInfo

class ServiceProviderPesrsonalInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProviderPersonalInfo
        exclude = ['id', 'created', 'Update']
class ServiceProviderWorkInfoSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()

    class Meta:
        model = ServiceProviderWorkInfo
        exclude = ['created', 'status']

    def get_personal_info(self, obj):
        personal_info = obj.personal_info
        if personal_info:
            personal_info_serializer = ServiceProviderPesrsonalInfoSerializer(personal_info)
            return personal_info_serializer.data
        else:
            return None
class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientInfo
        fields = '__all__'
class RequestServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'