from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    ID_number = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)
    photo = serializers.ImageField(  
        max_length=None,  
        allow_empty_file=False,  
        use_url=True,  
        write_only=True, 
    )
    profession = serializers.CharField(write_only=True)
    location = serializers.CharField(write_only=True)
    year_of_experince = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'ID_number', 'phone_number', 'password', 'password2', 'photo', 'profession', 'location', 'year_of_experience']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password2': 'Passwords do not match'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})
        
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            ID_number=self.validated_data['ID_number'],
            phone_number=self.validated_data['phone_number'],
            photo=self.validate_data['photo'],
            profession=self.validate_data['profession'],
            location=self.validate_data['location'],
            year_of_experience=self.validate_data['year_of_experience']
        )
        account.set_password(password)
        account.save()
        
        return account

class ServiceProLoginSerializer(serializers.ModelSerializer):
    
      class Meta:
        model = User
        fields = ('id', 'username', 'email')