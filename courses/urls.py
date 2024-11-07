from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet

app_name = CoursesConfig.name


router = DefaultRouter()
router.register(r'courses', viewset=CourseViewSet, basename='courses')
urlpatterns = [

] + router.urls
