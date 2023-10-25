from django.contrib import admin
from dashboard.models import ServiceProviderWorkInfo, ServiceProviderPersonalInfo, ServiceRequest, ClientInfo

# Register your models here.
admin.site.register(ServiceProviderPersonalInfo)
admin.site.register(ServiceProviderWorkInfo)
admin.site.register(ServiceRequest)
admin.site.register(ClientInfo)