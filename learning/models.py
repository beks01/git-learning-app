from django.db import models

# Список доступных языков
LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('ru', 'Russian'),
    ('ge', 'German'),
]


class GitCommand(models.Model):
    name = models.CharField(max_length=100)
    command = models.CharField(max_length=255)
    description = models.TextField()
    example = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')

    def __str__(self):
        return f"{self.name} ({self.language})"


class GitLesson(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')
    steps = models.JSONField(help_text="Список шагов урока (как массив объектов с полями step_number, description, explanation и example)")

    def __str__(self):
        return f"{self.title} ({self.language})"


class GitQuiz(models.Model):
    question = models.TextField()
    choices = models.JSONField(help_text="Список вариантов ответа (JSON-массив)")
    correct_answer = models.CharField(max_length=100)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')

    def __str__(self):
        return f"{self.question} ({self.language})"
