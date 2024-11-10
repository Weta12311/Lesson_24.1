from django.urls import path
from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', viewset=UserViewSet, basename='users')
router.register(r'payment', viewset=PaymentViewSet, basename='payment')

urlpatterns = [

] + router.urls