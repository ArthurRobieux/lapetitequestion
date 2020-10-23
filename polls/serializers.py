from rest_framework import serializers

from django.contrib.auth.models import User, Group
from polls.models import Poll, Question, Choice, Answer, AnswerChoice


class CreateAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    text = serializers.CharField(required=False, allow_blank=True)
    choice_ids = serializers.ListField(child=serializers.IntegerField(), required=False)


class CreateAnswersSerializer(serializers.Serializer):
    name = serializers.CharField()
    answers = CreateAnswerSerializer(many=True)


class AnswerChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = ["choice_id"]


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    choices = AnswerChoiceSerializer(many=True)

    class Meta:
        model = Answer
        fields = ["name", "text", "choices"]


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
