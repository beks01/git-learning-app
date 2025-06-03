from django.contrib import admin
from .models import GitCommand, GitLesson, GitQuiz


@admin.register(GitCommand)
class GitCommandAdmin(admin.ModelAdmin):
    list_display = ('name', 'command', 'language', 'description')
    search_fields = ('name', 'command')
    list_filter = ('language',)


@admin.register(GitLesson)
class GitLessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    list_filter = ('language',)
    search_fields = ('title',)

    # Показываем количество шагов (для удобства)
    def step_count(self, obj):
        return len(obj.steps) if obj.steps else 0

    step_count.short_description = 'Number of Steps'


@admin.register(GitQuiz)
class GitQuizAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'formatted_choices', 'correct_answer')
    search_fields = ('question', 'correct_answer')
    list_filter = ('language',)

    def formatted_choices(self, obj):
        return ", ".join(obj.choices)

    formatted_choices.short_description = 'Choices'
