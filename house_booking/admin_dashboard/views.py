from django.shortcuts import render
from rest_framework import viewsets
from .models import House, Booking, Review
from .serializers import HouseSerializer, BookingSerializer, ReviewSerializer
# Create your views here.

class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
