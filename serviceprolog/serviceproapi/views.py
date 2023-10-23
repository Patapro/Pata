from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


from django.contrib.auth import authenticate, login

from serviceprolog.serviceproapi.serializer import RegistrationSerializer, ServiceProLoginSerializer



@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['POST'])
def Registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            account = serializer.save()
            # refresh = RefreshToken.for_user(account)
            data = {
                'response': 'Registration successful!',
                'username': account.username,
                'email': account.email,
                'ID': account.ID_number,
                'phone_number': account.phone_number,
                'photo': account.photo,
                'profession': account.profession,
                'location': account.location,
                'year_of_experience': account.year_of_experience,
                # 'token': Token.objects.get(user=account).key
                
            }
            
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
def ServiceProLogin(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = ServiceProLoginSerializer(user)
            return Response(serializer.data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)