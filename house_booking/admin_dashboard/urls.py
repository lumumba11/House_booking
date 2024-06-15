from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseViewSet, BookingViewSet, ReviewViewSet
from dj_rest_auth.views import LoginView


router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]

