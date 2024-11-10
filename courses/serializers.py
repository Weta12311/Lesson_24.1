from rest_framework import serializers

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lessons_in_course = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lessons', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_count_lessons_in_course(self, instance):
        return instance.lessons.count()


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons_in_course = serializers.SerializerMethodField()

    def get_count_lessons_in_course(self, course):
        return Lesson.objects.filter(course=course.id).count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'preview', 'count_lessons_in_course')



