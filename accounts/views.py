from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, UserProfileSerializer
from dj_rest_auth.views import  PasswordResetView, PasswordResetConfirmView
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import CustomUserSerializer  # Import your custom user serializer
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer




# User sign-up view
class UserSignUpView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'key': token.key,
            'message': f'Successfully signed up as {user.username}'
        }, status=status.HTTP_201_CREATED)
    


# User login view
class UserLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # User is authenticated, get or create a token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'key': token.key,  # Token key
                'message': f'Successfully logged in as {username}'  # Success message
            }, status=status.HTTP_200_OK)
        
        # Authentication failed
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
  

# Password reset view
class CustomPasswordResetView(PasswordResetView):
    permission_classes = [AllowAny]

# Password reset confirmation view
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    permission_classes = [AllowAny]




# Social authentication views
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

    def post(self, request, *args, **kwargs):
        access_token = request.data.get('access_token')
        if not access_token:
            return Response({"error": "Access token required."}, status=status.HTTP_400_BAD_REQUEST)

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            # Check if user exists; if not, create them
            user_info = self.adapter_class.get_user_info(access_token)
            email = user_info.get('email')
            username = user_info.get('name')  # You can customize this as needed

            # Check if user already exists
            if not CustomUser.objects.filter(email=email).exists():
                CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=CustomUser.objects.make_random_password(),  # Auto-generate password
                    role='football_player'  # Set a default role or customize this logic
                )

        return response
    


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

    def post(self, request, *args, **kwargs):
        access_token = request.data.get('access_token')
        if not access_token:
            return Response({"error": "Access token required."}, status=status.HTTP_400_BAD_REQUEST)

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            # Check if user exists; if not, create them
            user_info = self.adapter_class.get_user_info(access_token)
            email = user_info.get('email')
            username = user_info.get('name')  # You can customize this as needed

            # Check if user already exists
            if not CustomUser.objects.filter(email=email).exists():
                CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=CustomUser.objects.make_random_password(),  # Auto-generate password
                    role='football_player'  # Set a default role or customize this logic
                )

        return response