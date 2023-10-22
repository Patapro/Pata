from django.urls import path
from admin_user.adminapi.views import AdminLoginView

urlpatterns = [
    path('logadmin/', AdminLoginView.as_view(), name='admin-login'),
]
