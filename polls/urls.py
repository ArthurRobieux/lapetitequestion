from django.urls import path

from . import views

from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path("polls/", views.polls_view, name="polls_view"),
    path("questions/", views.questions_view, name="questions_view"),
]