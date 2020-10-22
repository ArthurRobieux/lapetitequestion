from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from polls.models import Poll, Question, Choice
from polls.serializers import PollSerializer, QuestionSerializer, ChoiceSerializer


@api_view(["GET", "POST"])
def questions_view(request):
    if request.method == "GET":
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = QuestionSerializer(data=request.data)
        print("SERIALIZER", serializer)
        if serializer.is_valid():
            Question.objects.create(**serializer.data)

            return Response("Question created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def polls_view(request):
    if request.method == "GET":
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PollSerializer(data=request.data)
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