# Generated by Django 5.1.2 on 2024-11-10 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_lesson_course"),
        ("users", "0003_remove_user_country_user_city"),
    ]

    operations = [
        migrations.CreateModel(
            name="Paymant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pay_date",
                    models.DateField(blank=True, null=True, verbose_name="дата оплаты"),
                ),
                (
                    "payed_money",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="сумма оплаты"
                    ),
                ),
                (
                    "type_of_pay",
                    models.CharField(
                        choices=[("CASH", "CASH"), ("CARD", "CARD")],
                        max_length=5,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "payed_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="payed_course",
                        to="courses.course",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
