from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from polls.models import Poll, Question, Choice, Answer
from polls.serializers import (
    PollSerializer,
    QuestionSerializer,
    ChoiceSerializer,
    CreateAnswersSerializer,
)


# Polls


def handle_get_polls():
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


def handle_create_poll(data):

    serializer = PollSerializer(data=data)

    if serializer.is_valid():
        poll_data = serializer.data
        questions_data = poll_data.pop("questions")
        poll = Poll.objects.create(**poll_data)

        for question_data in questions_data:
            choices_data = question_data.pop("choices")
            question = Question.objects.create(poll=poll, **question_data)
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        return Response(poll.id, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Poll detail


def handle_get_poll_detail(poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        serializer = PollSerializer(poll)
        return Response(serializer.data)
    except:
        return Response("This poll doesn't exists", status=status.HTTP_400_BAD_REQUEST)


def handle_delete_poll(poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        poll.delete()
        return Response("Poll deleted", status=status.HTTP_200_OK)
    except:
        return Response("This poll doesn't exists", status=status.HTTP_400_BAD_REQUEST)


def handle_create_poll_answer(poll_id, answers_data):

    try:
        poll = Poll.objects.get(id=poll_id)
    except:
        return Response("This poll doesn't exists", status=status.HTTP_400_BAD_REQUEST)

    poll = Poll.objects.get(id=poll_id)
    serializer = CreateAnswersSerializer(data=answers_data, many=True)

    if serializer.is_valid():
        for answer_data in answers_data:
            print("LALALLA", answer_data)

            try:
                question_id = answer_data.pop("question_id")
                question = Question.objects.get(poll=poll, id=question_id)
                print("question", question)
                print("ADEZKFZRF", answer_data)

                Answer.objects.create(question=question, **answer_data)
            except:
                return Response(
                    "This question doesn't exists", status=status.HTTP_400_BAD_REQUEST
                )

        return Response("Answer created", status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
