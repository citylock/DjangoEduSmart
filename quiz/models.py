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
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, blank=False, help_text="a user friendly url")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    random_order = models.BooleanField(blank=False, default=False, help_text="Display the questions in a random order or as they set..")
    max_questions = models.PositiveIntegerField(blank=True, null=True, help_text="Number of questions to be answered on each attempt.")
    answers_at_end = models.BooleanField(blank=False, default=False, help_text="Correct answer is NOT shown after question. Answers displayed at the end.")
    exam_paper = models.BooleanField(blank=False, default=False, help_text="IF yes, the result of each attempt by a user will be stored. Necessary for marking")
    single_attempt = models.BooleanField(blank=False, default=False, help_text="IF yes, only one attemptby a user will be permitted.")

    class Meta: 
        verbose_name = 'quiz'
        verbose_name_plural = 'quizes'

    def __str__(self):
        return '{}'.format(self.title)


    
