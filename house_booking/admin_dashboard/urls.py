from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseViewSet, BookingViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
