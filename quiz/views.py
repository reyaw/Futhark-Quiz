from django.shortcuts import render
from quiz.models import Rune, Runes
from django.http import HttpResponse
from .forms import QuestionForm

posts = [
    {
        'author': 'Reya\'s dumb ass',
        'title': 'Blog post 1',
        'content': 'First post lol',
        'date_posted': 'April 12, 2021'
    },
    {
        'author': 'Its meeeeee',
        'title': 'Blog post 2',
        'content': 'titties titties titties titties titties',
        'date_posted': 'April 12, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    algiz = Rune(0)
    return render(request, 'quiz/home.html', context)


def about(request):
    return render(request, 'quiz/about.html', {'title': 'About'})


def get_answer(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            return "Correct"

    else:
        form = QuestionForm()
