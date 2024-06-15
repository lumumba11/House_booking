from rest_framework import serializers
from .models import House, Booking, Review
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from dj_rest_auth.serializers import PasswordResetSerializer as DefaultPasswordResetSerializer

#users preparations 
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create (self,validate_data):
         user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )   
         user.set_password(validated_data['password'])
         user.save()
         return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            }
        raise serializers.ValidationError('Invalid credentials')


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

      

class PasswordResetSerializer(DefaultPasswordResetSerializer):
    email = serializers.EmailField()

    def get_email_options(self):
        return {
            'email_template_name': 'password_reset_email.html',
            'subject_template_name': 'password_reset_subject.txt'
        }