from rest_framework import serializers
from .models import GitCommand, GitLesson, GitLessonStep, GitQuiz


class GitCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitCommand
        fields = '__all__'


class GitLessonStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitLessonStep
        fields = '__all__'


class GitLessonSerializer(serializers.ModelSerializer):
    steps = GitLessonStepSerializer(many=True, read_only=True)

    class Meta:
        model = GitLesson
        fields = '__all__'


class GitQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitQuiz
        fields = '__all__'
