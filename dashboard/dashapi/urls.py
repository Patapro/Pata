from django.urls import path
from dashboard.dashapi.views import Admindashboard, ServiceProviderPersonalInfoAV, ServiceProviderWorkInfoAV

urlpatterns = [
    # path('personalinfo/', ServiceProviderPersonalInfoAV.as_view(), name='personal-info'),
    # path('personalinfo/<int:pk>/', ServiceProviderPersonalInfoAV.as_view(), name='personal-info-detail'),
    # path('workinfo/', ServiceProviderWorkInfoAV.as_view(), name='work-info'),
    # path('workinfo/<int:pk>/', ServiceProviderWorkInfoAV.as_view(), name='work-info-detail'),
    path('admindashboard/', Admindashboard.as_view(), name='admind-dashboard'),
    path('admindashboard/<int:pk>/', Admindashboard.as_view(), name='admind-dashboard-toggled'),
]