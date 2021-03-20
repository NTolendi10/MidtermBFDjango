from django.urls import path
from main.views import BookJournalBaseViewSet, JournalApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('books', BookJournalBaseViewSet, basename='main')

urlpatterns = [
    path('journals/<int:pk>/', JournalApiView.as_view())
]

urlpatterns += router.urls
