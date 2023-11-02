from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from serviceprolog.serviceproapi.views import logout_view, Registration_view

urlpatterns = [
    path('serviceprologin/', obtain_auth_token, name='service-pro-login'),
    path('serviceprologout/', logout_view, name='service-pro-logout'),
    path('serviceproregister/', Registration_view, name='service-pro-register'),
]
