from django.db import models
from django.contrib.auth.models import User

class ServiceProviderPersonalInfo(models.Model):
    first_name=models.CharField(max_length=50, null=False)
    last_name=models.CharField(max_length=50, null=False)
    email=models.EmailField(max_length=100, null=False )
    phone_number = models.CharField(max_length=50, default='(+254) 000-0000', null=False)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ServiceProviderWorkInfo(models.Model):
    personal_info = models.OneToOneField(ServiceProviderPersonalInfo, on_delete=models.CASCADE, primary_key=True)
    profession=models.CharField(max_length=50, null=False)
    location=models.CharField(max_length=50, null=False)
    years_of_experince= models.IntegerField(default=0, null=False)
    
    def __str__(self):
        return self.profession