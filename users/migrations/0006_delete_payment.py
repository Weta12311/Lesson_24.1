# Generated by Django 5.1.2 on 2024-11-15 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_rename_paymant_payment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Payment",
        ),
    ]
