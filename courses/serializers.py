from rest_framework import serializers

from courses.models import Course, Lesson, Subscription
from courses.validators import validate_allowed_resources


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validate_allowed_resources])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons_in_course = serializers.SerializerMethodField()
    lesson = LessonSerializer(source="lessons", many=True)
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_lessons_in_course(self, instance):
        return instance.lessons.count()

    def get_subscription(self, instance):
        subscription = Subscription.objects.filter(
            course=instance, owner=self.context.get("request").user
        ).all()
        if subscription:
            return True
        else:
            return False


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons_in_course = serializers.SerializerMethodField()

    def get_count_lessons_in_course(self, course):
        return Lesson.objects.filter(course=course.id).count()

    class Meta:
        model = Course
        fields = ("title", "description", "preview", "count_lessons_in_course")


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["id", "owner", "course", "status"]
