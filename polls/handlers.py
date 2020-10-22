from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from polls.models import Poll, Question, Choice
from polls.serializers import PollSerializer, QuestionSerializer, ChoiceSerializer


def handle_get_polls():
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


def handle_create_poll(data):

    print("DATA", data)

    serializer = PollSerializer(data=data)

    print("SERIALIZER", serializer, serializer.is_valid())

    if serializer.is_valid():
        poll_data = serializer.data
        questions_data = poll_data.pop("questions")
        poll = Poll.objects.create(**poll_data)
        for question_data in questions_data:
            choices_data = question_data.pop("choices")
            question = Question.objects.create(poll=poll, **question_data)
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)

        return Response("Poll created", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
