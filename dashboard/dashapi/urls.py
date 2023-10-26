from django.urls import path
from dashboard.dashapi.views import (
    AdminDashBoard,
    ServiceProviderDashBoard,
    LandingPage,
    LandingPageServiceProviderSF,
    AdmindashboardServiceProviderSF,
    RequestService,
    ServiveProviderRequestInfo,
    ServiceProvierRequestApprove,
    AdminServiceProviderApproval,
    ApproveRequest,
    RejectRequest,
    ServiceProvidersAnalytics,
    PendingRequestAnalytics
    )

urlpatterns = [
    path('admindashboard/', AdminDashBoard.as_view(), name='admind-dashboard'),
    path('admindashboard/<int:pk>/', AdminDashBoard.as_view(), name='admind-dashboard-toggled'),
    path('serviceprovider/<int:pk>/', AdminDashBoard.as_view(), name='service-provider-delete'),
    path('serviceproviderdashboard/', ServiceProviderDashBoard.as_view(), name='service-provider-dashboard'),
    path('serviceproviderdashboard/<int:pk>/', ServiceProviderDashBoard.as_view(), name='service-provider-profile-updated'),
    path('landingpage/', LandingPage.as_view(), name='landing-page'),
    path('search/', LandingPageServiceProviderSF.as_view(), name='service-provider-search'),
    path('adsearch/', AdmindashboardServiceProviderSF.as_view(), name='ad-service-provider-search'),
    path('requestservice/', RequestService.as_view(), name='request-service'),
    path('serviceproviderrequestinfo/<int:client_id>/', ServiveProviderRequestInfo.as_view(), name='service-provider-request-info'),
    path('serviceproviderrequestapproval/<int:pk>/', ServiceProvierRequestApprove.as_view(), name='service-provider-request-approval'),
    path('adminrequestapproval/', AdminServiceProviderApproval.as_view(), name='admin-request-approval'),
    path('approve/<int:pk>/', ApproveRequest.as_view(), name='request-approval'),
    path('reject/<int:pk>/', RejectRequest.as_view(), name='request-reject'),
    path('serviceprovideranalytics/', ServiceProvidersAnalytics.as_view(), name='service-provider-analytics'),
    path('requestanalytics/', PendingRequestAnalytics.as_view(), name='request-analytics'),
]