from rest_framework.serializers import ValidationError

allowed_resources = "youtube.com"


def validate_allowed_resources(value):
    if value != "null":
        if allowed_resources not in value:
            raise ValidationError("Использованы запрещенные ресурсы")
