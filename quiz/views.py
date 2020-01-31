from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Question

# Create your views here.
def index(request): 
    text_var = "This is my first Django app web response!!"
    return HttpResponse(text_var)

def allQuiz(request, q_slug=None):
    # q_slug : quiz url
    q_page = None
    questions = None
    if q_slug != None: 
        q_page = get_object_or_404(Quiz, slug=q_slug)
    return render(request, 'quiz/quiz.html', {'quiz': q_page})




