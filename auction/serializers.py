from rest_framework import serializers

from .models import Item, Bid, Question, Answer
from users.models import CustomUser

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'user',
            'title',
            'starting_price',
            'description',
            'item_image',
            'end_date',
            'end_time'
            ]

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = [
            'id',
            'user',
            'item',
            'amount'
            ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'user',
            'item',
            'question'
            ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'user',
            'item',
            'question',
            'answer'
            ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'dob',
            'profile_picture'
        ]