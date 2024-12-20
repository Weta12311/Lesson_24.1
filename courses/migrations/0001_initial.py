# Generated by Django 5.1.2 on 2024-11-07 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=250, verbose_name="title")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью",
                        null=True,
                        upload_to="courses/previews/",
                        verbose_name="previews",
                    ),
                ),
                ("description", models.TextField(verbose_name="description")),
            ],
            options={
                "verbose_name": "курс",
                "verbose_name_plural": "курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("title", models.CharField(max_length=250, verbose_name="title")),
                ("description", models.TextField(verbose_name="description")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите превью",
                        null=True,
                        upload_to="courses/lessons/previews/",
                        verbose_name="previews",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберете курс, к которому относится урок",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="course",
                        to="courses.course",
                        verbose_name="Курс к которому относится урок",
                    ),
                ),
            ],
        ),
    ]
