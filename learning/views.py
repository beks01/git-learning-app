from rest_framework import viewsets
from .models import GitCommand, GitLesson, GitQuiz
from .serializers import GitCommandSerializer, GitLessonSerializer, GitQuizSerializer

class GitCommandViewSet(viewsets.ModelViewSet):
    queryset = GitCommand.objects.all()
    serializer_class = GitCommandSerializer

class GitLessonViewSet(viewsets.ModelViewSet):
    queryset = GitLesson.objects.all()
    serializer_class = GitLessonSerializer

class GitQuizViewSet(viewsets.ModelViewSet):
    queryset = GitQuiz.objects.all()
    serializer_class = GitQuizSerializer
