from django.contrib import admin

from .models import Category, Quiz
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = { 'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ['slug', 'category','qtype', 'question', 'question_image', 'difficulty', 'hint','created', 'updated']
    list_editable = ['category', 'qtype', 'question', 'question_image', 'difficulty', 'hint']
    prepopulated_fields = {'slug': ('number', 'question',)}
    list_per_page = 20

admin.site.register(Quiz, QuizAdmin)
