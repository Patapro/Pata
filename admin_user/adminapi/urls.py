from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from admin_user.adminapi.views import logout_view

urlpatterns = [
    path('adminlogin/', obtain_auth_token, name='admin-login'),
    path('adminlogout/',logout_view, name='admin-login'),
    
]
