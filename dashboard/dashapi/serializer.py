from rest_framework import serializers
from dashboard.models import ServiceProviderPersonalInfo, ServiceProviderWorkInfo

class ServiceProviderPesrsonalInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProviderPersonalInfo
        exclude = ['created', 'Update']
        
class ServiceProviderWorkInfoSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()

    class Meta:
        model = ServiceProviderWorkInfo
        fields = '__all__'

    def get_personal_info(self, obj):
        personal_info = obj.personal_info
        if personal_info:
            personal_info_serializer = ServiceProviderPesrsonalInfoSerializer(personal_info)
            return personal_info_serializer.data
        else:
            return None
