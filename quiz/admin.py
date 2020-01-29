from django.contrib import admin

from .models import Category, Quiz, Question, Answer
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Category, CategoryAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['content']

admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'content', 'correct']

admin.site.register(Answer, AnswerAdmin)
