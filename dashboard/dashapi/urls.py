from django.urls import path
from dashboard.dashapi.views import (
    AdminDashBoard,
    # ServiceProviderPersonalInfoAV, 
    # ServiceProviderWorkInfoAV,
    ServiceProviderDashBoard,
    LandingPage,
    ServiceProviderSF,
    )

urlpatterns = [
    # path('personalinfo/', ServiceProviderPersonalInfoAV.as_view(), name='personal-info'),
    # path('personalinfo/<int:pk>/', ServiceProviderPersonalInfoAV.as_view(), name='personal-info-detail'),
    # path('workinfo/', ServiceProviderWorkInfoAV.as_view(), name='work-info'),
    # path('workinfo/<int:pk>/', ServiceProviderWorkInfoAV.as_view(), name='work-info-detail'),
    path('admindashboard/', AdminDashBoard.as_view(), name='admind-dashboard'),
    path('admindashboard/<int:pk>/', AdminDashBoard.as_view(), name='admind-dashboard-toggled'),
    path('serviceprovider/<int:pk>/', AdminDashBoard.as_view(), name='service-provider-delete'),
    path('serviceproviderdashboard/', ServiceProviderDashBoard.as_view(), name='service-provider-dashboard'),
    path('serviceproviderdashboard/<int:pk>/', ServiceProviderDashBoard.as_view(), name='service-provider-profile-updated'),
    path('landingpage/', LandingPage.as_view(), name='landing-page'),
    path('search/', ServiceProviderSF.as_view(), name='service-provider-search'),
]