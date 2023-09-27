from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from dashboard.dashapi.serializer import serializers
from dashboard import models

class ServiceProviderPersonalInfoTestCase(APITestCase):
    
    def setUp(self):
        self.personal_info = models.ServiceProviderPersonalInfo.objects.create(first_name='peter', last_name='martin', email='martin@gmail.com', phone_number='740190783')
    
    def test_serviceproviderpersonalinfo_create(self):
        data = {
            'first_name' : 'Peter',
            'last_name' : 'Martin',
            'email' : 'peter@gmail.com',
            'phone_number' : '740190783'
        }
        response = self.client.post(reverse('personal-info'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_serviceproviderpersonalinfo_update(self):
        data={
            'first_name' : 'Peter',
            'last_name' : 'Kirika',
            'email' : 'martin@gmail.com',
            'phone_number' : '740190783',
        }
        response = self.client.put(reverse('personal-info-detail', args=(self.personal_info.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class ServiceProviderWorkInfoTestCase(APITestCase):
    
    def setUp(self):
        self.personal_info = models.ServiceProviderPersonalInfo.objects.create(first_name='peter', last_name='martin', email='martin@gmail.com', phone_number='740190783')
        
        self.work_info = models.ServiceProviderWorkInfo.objects.create(personal_info=self.personal_info, profession='Plumber', location='juja', years_of_experience=4)
    
    def test_serviceproviderworkinfo_create(self):
        data = {
            'personal_info' : 1,
            'profession' : 'plumber',
            'location' : 'juja',
            'years_of_experience' : 4
        }
        response = self.client.post(reverse('work-info'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serviceproviderworkinfo_update(self):
        data = {
            'personal_info' : self.personal_info.id,
            'profession' : 'Electrician',
            'location' : 'juja',
            'years_of_experience' : 4
        }
        response = self.client.put(reverse('work-info-detail', args=(self.work_info.pk,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)