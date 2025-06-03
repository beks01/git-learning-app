from rest_framework import serializers
from .models import GitCommand, GitLesson, GitQuiz


class GitCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitCommand
        fields = '__all__'


class GitLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitLesson
        fields = '__all__'


class GitQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitQuiz
        fields = '__all__'
