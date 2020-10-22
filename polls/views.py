from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from polls.models import Poll, Question, Choice
from polls.serializers import PollSerializer, QuestionSerializer, ChoiceSerializer
from polls.handlers import (
    handle_get_polls,
    handle_create_poll,
    handle_get_poll_detail,
    handle_get_questions,
    handle_create_question,
    handle_get_question_detail,
)


@api_view(["GET", "POST"])
def questions_view(request):
    if request.method == "GET":
        return handle_get_questions()

    elif request.method == "POST":
        return handle_create_question(request.data)


@api_view(["GET"])
def question_detail_view(request, question_id=None):
    if request.method == "GET":
        return handle_get_question_detail(question_id)


@api_view(["GET", "POST"])
def polls_view(request):
    if request.method == "GET":
        return handle_get_polls()

    elif request.method == "POST":
        return handle_create_poll(request.data)


@api_view(["GET"])
def poll_detail_view(request, poll_id=None):
    if request.method == "GET":
        return handle_get_poll_detail(poll_id)
