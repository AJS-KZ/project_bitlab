from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, LoginViewSet, LogoutViewSet


router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view()),
    path('logout/', LogoutViewSet.as_view()),
] + router.urls
