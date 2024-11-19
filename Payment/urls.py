from rest_framework.routers import DefaultRouter

from Payment.apps import PaymentConfig
from Payment.views import PaymentViewSet

app_name = PaymentConfig.name

router = DefaultRouter()
router.register(r"payment", viewset=PaymentViewSet, basename="payment")
router.register(r"subscription", viewset=SubscriptionViewSet, basename="subscription")
