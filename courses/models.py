from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name="title")
    preview = models.ImageField(
        upload_to="courses/previews/",
        verbose_name="previews",
        blank=True,
        null=True,
        help_text="Загрузите превью",
    )
    description = models.TextField(verbose_name="description")
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=250, verbose_name="title")
    description = models.TextField(verbose_name="description")
    preview = models.ImageField(
        upload_to="courses/lessons/previews/",
        verbose_name="previews",
        blank=True,
        null=True,
        help_text="Загрузите превью",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс к которому относится урок",
        help_text="Выберете курс, к которому относится урок",
        blank=True,
        null=True,
        related_name="lessons",
    )
    link = models.URLField(max_length=200, blank=True, null=True, verbose_name="link")

    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    """
    Модель подписки на курс
    """

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="владелец",
        related_name="subscription",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="курс",
        related_name="subscriptions",
    )
    status = models.BooleanField(
        default=False, verbose_name="статус подписки", **NULLABLE
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"{self.owner}: {self.course}"
