from django.urls import path

from . import views

from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path("polls/", views.polls_view, name="polls_view"),
    path("polls/<int:poll_id>/", views.poll_detail_view, name="poll_detail_view"),
    path("questions/", views.questions_view, name="questions_view"),
    path(
        "questions/<int:question_id>/",
        views.question_detail_view,
        name="question_detail_view",
    ),
]