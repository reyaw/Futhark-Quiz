from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(template_name='home.html'), name='quiz-home'),
    path('about/', views.about, name='quiz-about'),
    # path("get_answer/", views.get_answer("POST"))
]
