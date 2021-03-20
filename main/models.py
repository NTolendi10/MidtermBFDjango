from django.db import models


# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField(max_length=15, blank=True)
    description = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(max_length=4, blank=True)
    genre = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class Journal(BookJournalBase):
    CHOICES = [
        'Bullet',
        'Food',
        'Travel',
        'Sport'
    ]
    type = models.CharField(max_length=50, choices=CHOICES)
    publisher = models.CharField(max_length=50, blank=True)

    objects = BookJournalBase()

    class Meta:
        verbose_name = 'journal'
        verbose_name_plural = 'journals'
