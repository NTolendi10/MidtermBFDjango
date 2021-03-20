from rest_framework import serializers
from main.models import BookJournalBase, Book, Journal


class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookJournalBase
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class JournalSerializer(serializers.ModelSerializer):
    journals = BookSerializer(many=True)

    class Meta:
        model = Journal
        fields = '__all__'