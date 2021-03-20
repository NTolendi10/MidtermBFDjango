from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from main.models import BookJournalBase, Book, Journal
from main.serializers import BookSerializer, JournalSerializer, BookJournalBaseSerializer


class BookJournalBaseViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookJournalBaseSerializer

    def get_queryset(self):
        return Book.objects.all()

    @action(methods=['GET'], detail=False, url_path='inactive', url_name='in_active', permission_classes=(AllowAny,))
    def not_active(self, request):
        # queryset = Book.objects.filter(is_active=False)
        serializer = BookJournalBaseSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class JournalApiView(generics.RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class BookViewSet(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
