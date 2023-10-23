from django.urls import path
from serviceprolog.serviceproapi.views import ServiceProLogin

urlpatterns = [
    path('serviceprologin/', ServiceProLogin, name='service-pro-login'),
]
