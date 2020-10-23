from rest_framework import serializers

from django.contrib.auth.models import User, Group
from polls.models import Poll, Question, Choice, Answer


class CreateAnswersSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    name = serializers.CharField()
    text = serializers.CharField(required=False)
    choice_ids = serializers.IntegerField(required=False)


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ["name", "text"]


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "description"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choices = ChoiceSerializer(many=True, required=False)
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ["id", "description", "question_type", "choices", "answers"]


class PollSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ["id", "title", "description", "created_at", "questions"]
