from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

from users.views import (
    UserCreateAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView, SubscriptionAPIView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = UsersConfig.name

router = DefaultRouter()


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_get"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user_delete"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path('courses/<int:pk>/subscription/', SubscriptionAPIView.as_view(),
         name='subscription'),
] + router.urls
