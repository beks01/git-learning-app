from rest_framework import viewsets
from .models import GitCommand, GitLesson, GitQuiz
from .serializers import GitCommandSerializer, GitLessonSerializer, GitQuizSerializer

class GitCommandViewSet(viewsets.ModelViewSet):
    queryset = GitCommand.objects.all()
    serializer_class = GitCommandSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language')
        if language:
            return self.queryset.filter(language=language)
        return self.queryset

class GitLessonViewSet(viewsets.ModelViewSet):
    queryset = GitLesson.objects.all()
    serializer_class = GitLessonSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language')
        if language:
            return self.queryset.filter(language=language)
        return self.queryset

class GitQuizViewSet(viewsets.ModelViewSet):
    queryset = GitQuiz.objects.all()
    serializer_class = GitQuizSerializer

    def get_queryset(self):
        language = self.request.query_params.get('language')
        if language:
            return self.queryset.filter(language=language)
        return self.queryset
