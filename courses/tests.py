from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Тестовый пользователь
        """
        self.user = User(
            email="test@test.ru",
            phone="111111111",
            city="Testograd",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )
        self.user.set_password("123QWE456RTY")
        self.user.save()

        response = self.client.post(
            "/users/login/", {"email": "test@test.ru", "password": "123QWE456RTY"}
        )

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

        self.course = Course.objects.create(title="test_course", owner=self.user)

        # Создаем тестовый урок
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="This is a test lesson",
            course=self.course,
            owner=self.user,
        )

    def test_create_lesson(self):
        """
        Тест операции создания (create) проверки создания уроков
        """
        data = {
            "title": "test",
            "course": 1,
            "link": "https://www.youtube.com/",
            "description": "test description",
            "owner": self.user.id,
        }
        create_lesson = reverse("courses:lesson_create")
        response = self.client.post(create_lesson, data, format="json", **self.headers)
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["title"], data["title"])

    def test_retrieve_lesson(self):
        """
        Тест операции чтения (retrieve) урока
        """
        retrieve_url = reverse("courses:lesson_detail", args=[self.lesson.id])
        response = self.client.get(retrieve_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.lesson.title)

    def test_update_lesson(self):
        """
        Тест операции обновления (update) урока
        """
        update_url = reverse("courses:lesson_update", args=[self.lesson.id])
        updated_data = {
            "title": "Updated Lesson",
            "description": "This is an updated lesson",
        }
        response = self.client.patch(update_url, updated_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.lesson.refresh_from_db()
        self.assertEqual(self.lesson.title, updated_data["title"])
        self.assertEqual(self.lesson.description, updated_data["description"])

    def test_delete_lesson(self):
        """
        Тест операции удаления (delete) урока
        """
        delete_url = reverse("courses:lesson_delete", args=[self.lesson.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.filter(id=self.lesson.id).exists())

    def test_list_lesson(self):
        """
        Тест операции получения списка уроков
        """
        list_url = reverse("courses:lesson_list")
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["title"], self.lesson.title)


class CourseTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Тестовый пользователь
        """
        self.user = User(
            email="test@test.ru",
            phone="111111111",
            city="Testograd",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        self.user.set_password("123QWE456RTY")
        self.user.save()

        response = self.client.post(
            "/users/login/", {"email": "test@test.ru", "password": "123QWE456RTY"}
        )

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

        # Тестовый курс
        self.course = Course.objects.create(
            title="test_course",
            owner=self.user,
        )

        # Создаем тестовый урок
        self.lesson = Lesson.objects.create(
            title="Test Lesson",
            description="This is a test lesson",
            course=self.course,
            owner=self.user,
        )

        # Создаем тестовую подписку
        self.subscribe = Subscription.objects.create(
            owner=self.user, course=self.course
        )

    def test_list_course(self):
        """
        Тест операции получения списка уроков
        """
        course_url = reverse("courses:courses-list")
        response = self.client.get(course_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["title"], self.course.title)


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        """
        Тестовый пользователь
        """
        self.user = User(
            email="test@test.ru",
            phone="111111111",
            city="Testograd",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        self.user.set_password("123QWE456RTY")
        self.user.save()

        response = self.client.post(
            "/users/login/", {"email": "test@test.ru", "password": "123QWE456RTY"}
        )

        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.headers = {"HTTP_AUTHORIZATION": f"Bearer {self.access_token}"}

        # Тестовый курс
        self.course = Course.objects.create(
            title="test_course",
            owner=self.user,
        )

        # Создаем тестовую подписку
        self.subscribe = Subscription.objects.create(
            owner=self.user,
            course=self.course,
        )

    def test_subscribe_to_course(self):
        """
        Тест операции создания подписки на курс
        """
        subscribe_url = reverse("courses:subscription", args=[self.course.id])
        print(subscribe_url)
        response = self.client.post(subscribe_url, {}, format="json", **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Вы подписались на курс.")

    def test_unsubscribe_from_course(self):
        """
        Тест операции отписки от курса
        """
        subscribe_url = reverse("courses:subscription", args=[self.course.id])
        response = self.client.post(subscribe_url, {}, format="json", **self.headers)
        response = self.client.post(subscribe_url, {}, format="json", **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Вы отписались от курса.")
