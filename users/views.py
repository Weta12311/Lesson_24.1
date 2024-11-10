from django.shortcuts import render
from rest_framework import viewsets, filters

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filterset_fields = ('payed_course', 'type_of_pay')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ('pay_date',)

