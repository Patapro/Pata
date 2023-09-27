from django.contrib import admin
from dashboard.models import ServiceProviderWorkInfo, ServiceProviderPersonalInfo

# Register your models here.
admin.site.register(ServiceProviderPersonalInfo)
admin.site.register(ServiceProviderWorkInfo)