from django.shortcuts import render
from rest_framework import viewsets, filters, serializers

from Payment.models import Payment
from Payment.serializers import PaymentSerializer
from Payment.services import create_stripe_price, create_stripe_session


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filterset_fields = ("payed_course", "type_of_pay")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ("pay_date",)

    def perform_create(self, serializer):
        course = serializer.validated_data.get('paid_course')
        if not course:
            raise serializers.ValidationError('Укажите курс')
        payment = serializer.save()
        stripe_price_id = create_stripe_price(payment)
        payment.payment_url, payment.payment_id = (
            create_stripe_session(stripe_price_id)
        )
        payment.save()
