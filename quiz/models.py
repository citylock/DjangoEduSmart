from django.db import models

# Create your models here.


class Category(models.Model):
    # Type of exam : opportunity class, selective, naplan, ... 
    category = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    class Meta: 
        ordering = ('category', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.category)


class Quiz(models.Model): 
    title = models.CharField(max_length=200 unique=True)
    