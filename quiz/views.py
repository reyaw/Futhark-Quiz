from django.shortcuts import render
from quiz.models import Rune, Runes
from django.http import HttpResponse
from .forms import QuestionForm
from django.views.generic import TemplateView

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


class HomePageView(TemplateView):
    # context = {
    #     'posts': posts
    # }
    # algiz = Rune(0)
    #  return render(request, 'quiz/home.html', context)
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {'title': "Quiz Home"}



def about(request):
    return render(request, 'quiz/about.html', {'title': 'About'})
