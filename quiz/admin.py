from django.contrib import admin

from .models import Category, Quiz
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(Category, CategoryAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Quiz, QuizAdmin)
