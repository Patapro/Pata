from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from dashboard.dashapi.serializer import serializers
from dashboard import models

# class ServiceProviderPersonalInfoTestCase(APITestCase):
    
#     def setUp(self):
#         self.personal_info = models.ServiceProviderPersonalInfo.objects.create(first_name='peter', last_name='martin', email='martin@gmail.com', phone_number='740190783')
    
#     def test_serviceproviderpersonalinfo_create(self):
#         data = {
#             'first_name' : 'Peter',
#             'last_name' : 'Martin',
#             'email' : 'peter@gmail.com',
#             'phone_number' : '740190783'
#         }
#         response = self.client.post(reverse('personal-info'), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_serviceproviderpersonalinfo_update(self):
#         data={
#             'first_name' : 'Peter',
#             'last_name' : 'Kirika',
#             'email' : 'martin@gmail.com',
#             'phone_number' : '740190783',
#         }
#         response = self.client.put(reverse('personal-info-detail', args=(self.personal_info.id,)), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
# class ServiceProviderWorkInfoTestCase(APITestCase):
    
#     def setUp(self):
#         self.personal_info = models.ServiceProviderPersonalInfo.objects.create(first_name='peter', last_name='martin', email='martin@gmail.com', phone_number='740190783')
        
#         self.work_info = models.ServiceProviderWorkInfo.objects.create(personal_info=self.personal_info, profession='Plumber', location='juja', years_of_experience=4)
    
#     def test_serviceproviderworkinfo_create(self):
#         data = {
#             'personal_info' : 1,
#             'profession' : 'plumber',
#             'location' : 'juja',
#             'years_of_experience' : 4
#         }
#         response = self.client.post(reverse('work-info'), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_serviceproviderworkinfo_update(self):
#         data = {
#             'personal_info' : self.personal_info.id,
#             'profession' : 'Electrician',
#             'location' : 'juja',
#             'years_of_experience' : 4
#         }
#         response = self.client.put(reverse('work-info-detail', args=(self.work_info.pk,)), data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)



# class AdminApprovalTest(APITestCase):
#     def setUp(self):
#         # Create an admin user
#         self.admin_user = User.objects.create_user(username='admin', password='password')
#         self.admin_user.is_staff = True
#         self.admin_user.save()

#         # Create a client
#         self.client = models.ServiceProviderWorkInfo(name='Client Name', client_approved=False)

#     def test_admin_approve_client(self):
#         # Log in as the admin user
#         self.client.login(username='admin', password='password')

#         # Get the client detail page (adjust the URL to match your project's URL structure)
#         response = self.client.get(f'/admin/yourapp/client/{self.client.id}/change/')

#         # Check that the response status code is 200 (OK)
#         self.assertEqual(response.status_code, 200)

#         # Simulate clicking the 'client_approved' checkbox
#         response = self.client.post(f'/admin/yourapp/client/{self.client.id}/change/', {
#             'client_approved': 'on'  # Assumes the field name is 'client_approved'
#         })

#         # Check that the response status code is 302 (Redirect after successful update)
#         self.assertEqual(response.status_code, 302)

#         # Refresh the client object from the database to get the updated value
#         self.client.refresh_from_db()

#         # Check that the 'client_approved' field is now True
#         self.assertTrue(self.client.client_approved)
