from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import House, Booking, Review
from .serializers import (
    HouseSerializer,
    BookingSerializer,
    ReviewSerializer,
    LoginSerializer,
    SignupSerializer
)
from dj_rest_auth.registration.views import RegisterView as DefaultRegisterView
from allauth.account.views import SignupView as AllauthSignupView


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Perform login logic here if needed
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer


class CustomRegisterView(DefaultRegisterView):
    # Custom code here if needed
    pass
