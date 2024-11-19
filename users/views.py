from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from courses.models import Course, Subscription
from courses.serializers import SubscriptionSerializer
from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()


class SubscriptionAPIView(APIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, *args, **kwargs):

        course = Course.objects.get(pk=self.kwargs['pk'])
        user = self.request.user
        subscription = Subscription.objects.filter(course=course,
                                                   owner=user).first()

        if subscription.status:
            subscription.status = False
            subscription.save()
            message = 'Вы отписались от курса.'
        else:
            subscription.status = True
            subscription.save()
            message = 'Вы подписались на курс.'

        return Response({"message": message})
