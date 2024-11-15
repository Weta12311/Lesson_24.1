from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course
from users.models import User


class Payment(models.Model):
    class TypeOfPay(models.TextChoices):
        CASH = "CASH", "CASH"
        CARD = "CARD", "CARD"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
    )
    pay_date = models.DateField(
        verbose_name="дата оплаты",
        blank=True,
        null=True,
    )
    payed_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="payed_course",
        blank=True,
        null=True,
    )
    payed_money = models.PositiveIntegerField(
        verbose_name="сумма оплаты", blank=True, null=True
    )
    type_of_pay = models.CharField(
        max_length=5, choices=TypeOfPay.choices, verbose_name="способ оплаты"
    )
