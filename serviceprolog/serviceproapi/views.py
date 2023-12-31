from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from serviceprolog.serviceproapi.serializer import RegistrationSerializer



@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response('Logout Successful', status=status.HTTP_200_OK)
    

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
                'token': Token.objects.get(user=account).key
                
            }
            
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)