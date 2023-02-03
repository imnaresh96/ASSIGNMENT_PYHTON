from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    Title = serializers.CharField(max_length=100)
    Author= serializers.CharField(max_length=50)
    Isbn = serializers.CharField(max_length=100)
    Publisher = serializers.CharField(max_length=100)