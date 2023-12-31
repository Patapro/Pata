from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class ServiceProviderPersonalInfo(models.Model):
    first_name = models.CharField(
        max_length=50,
        null=False,
        validators=[MinLengthValidator(limit_value=3, message="First name must be at least 3 characters.")]
    )

    last_name = models.CharField(
        max_length=50,
        null=False,
        validators=[MinLengthValidator(limit_value=3, message="Last name must be at least 3 characters.")]
    )
    email=models.EmailField(max_length=100, null=False )
    phone_number = models.CharField(max_length=50, default='(+254) 000-0000', null=False)
    Id_number = models.CharField(max_length=10, default='000-000-00', null=False)
    created = models.DateTimeField(default=timezone.now)
    Update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', default='default_photo.jpg')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ServiceProviderWorkInfo(models.Model):
    status = models.CharField(
        max_length=10,
        choices=[("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")],
        default="Pending"
    )
    personal_info = models.OneToOneField(ServiceProviderPersonalInfo, on_delete=models.CASCADE, primary_key=True, default=None)
    profession = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    years_of_experience = models.IntegerField(default=0, null=False)
    created = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.profession
    
class ClientInfo(models.Model):
    
    first_name = models.CharField(
        max_length=50,
        null=False,
        validators=[MinLengthValidator(limit_value=3, message="First name must be at least 3 characters.")]
    )

    last_name = models.CharField(
        max_length=50,
        null=False,
        validators=[MinLengthValidator(limit_value=3, message="Last name must be at least 3 characters.")]
    )
    phone_number = models.CharField(max_length=50, default='(+254) 000-0000', null=False)
    Id_number = models.CharField(max_length=10, default='000-000-00', null=False)
    Active = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    Update = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', default='default_photo.jpg')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ServiceRequest(models.Model):

    service_provider = models.ForeignKey(ServiceProviderPersonalInfo, on_delete=models.CASCADE, default=None)
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    service = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(default=timezone.now)
    Update = models.DateTimeField(auto_now=True)
    Active = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.service_provider} {self.service} {self.location} {self.client}"