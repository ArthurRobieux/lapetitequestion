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
    handle_delete_poll,
    handle_create_poll_answer,
)


@api_view(["GET", "POST"])
def polls_view(request):
    if request.method == "GET":
        return handle_get_polls()

    elif request.method == "POST":
        return handle_create_poll(request.data)


@api_view(["GET", "POST", "DELETE"])
def poll_detail_view(request, poll_id=None):
    if request.method == "GET":
        return handle_get_poll_detail(poll_id)

    elif request.method == "POST":
        return handle_create_poll_answer(poll_id, request.data)

    elif request.method == "DELETE":
        return handle_delete_poll(poll_id)


@api_view(["POST"])
def poll_answer_view(request, poll_id=None):
    if request.method == "POST":
        return handle_create_poll_answer(poll_id, request.data)
