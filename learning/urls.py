from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GitCommandViewSet, GitLessonViewSet, GitQuizViewSet

router = DefaultRouter()
router.register(r'commands', GitCommandViewSet)
router.register(r'lessons', GitLessonViewSet)
router.register(r'quizzes', GitQuizViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
