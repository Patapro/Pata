from rest_framework import serializers
from dashboard.models import ServiceProviderPersonalInfo, ServiceProviderWorkInfo

class ServiceProviderPesrsonalInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProviderPersonalInfo
        fields = '__all__'
        
class ServiceProviderWorkInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProviderWorkInfo
        fields = '__all__'
        
