from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from polls.models import Poll, Question, Choice
from polls.serializers import PollSerializer, QuestionSerializer, ChoiceSerializer


# Questions


def handle_get_questions():
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


def handle_create_question(data):
    serializer = QuestionSerializer(data=data)
    if serializer.is_valid():
        Question.objects.create(**serializer.data)

        return Response("Question created", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def handle_get_question_detail(question_id):
    question = Question.objects.get(id=question_id)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)


# Polls


def handle_get_polls():
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


def handle_create_poll(data):
    serializer = PollSerializer(data=data)
    if serializer.is_valid():
        questions_data = serializer.data.pop("questions")
        Poll.objects.create(**serializer.data)
        for question_data in questions_data:
            choices_data = question_data.pop("choices")
            question = Question.objects.create(poll=poll, **question_data)
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        return Response("Poll created", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def handle_get_poll_detail(poll_id):
    poll = Poll.objects.get(id=poll_id)
    serializer = PollSerializer(poll)
    return Response(serializer.data)
