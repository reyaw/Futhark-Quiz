from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('about/', views.about, name='quiz-about'),
    path("get_answer/", views.get_answer("POST"))
]
