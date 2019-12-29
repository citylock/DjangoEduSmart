from django.db import models

# Create your models here.

class Category(models.Model):
    # Type of exam : opportunity class, selective, naplan, ... 
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta: 
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


class Quiz(models.Model):
    number = models.DecimalField(max_digits=10, decimal_places=0, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # qtype : text, image, .. 
    qtype = models.CharField(max_length=50)
    question = models.TextField()
    question_image = models.ImageField(upload_to="question", blank=True)
    difficulty = models.DecimalField(max_digits=10, decimal_places=1, default = 1000)
    hint = models.TextField(blank=True)
    created =  models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta: 
        ordering = ('id', )
        verbose_name = 'quiz'
        verbose_name_plural = 'quizes'

