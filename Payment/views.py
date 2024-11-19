from django.shortcuts import render
from rest_framework import viewsets, filters

from Payment.models import Payment
from Payment.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filterset_fields = ("payed_course", "type_of_pay")
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ("pay_date",)



