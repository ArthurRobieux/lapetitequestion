from rest_framework import serializers

from django.contrib.auth.models import User, Group
from polls.models import Poll, Question, Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "description", "votes"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "description", "question_type", "choices"]


class PollSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ["id", "title", "description", "created_at", "questions"]
