from rest_framework import serializers
from .models import *

class BookSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    Title = serializers.CharField(max_length=100)
    Author= serializers.CharField(max_length=50)
    Isbn = serializers.CharField(max_length=100)
    Publisher = serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Book.objects.create(**validated_data)