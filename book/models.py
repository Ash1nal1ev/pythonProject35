from os import name
from pyexpat import model
from statistics import mode
from turtle import title
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

class Raiting(models.Model):
    RATE_CHOICES = (
        (1, 'Bad'),
        (2, 'Okey'),
        (3, 'Fine'),
        (4, 'Good'),
        (5, 'Amaizing'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='raiting_book')
    name = models.CharField(max_length=100)
    raiting = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.book.title

class BookComment(models.Model):
    name = models.CharField(max_length=100)
    book_selection = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comment')
    text_comment = models.TextField()
    date_now = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.book_selection.title

class ExpertBook(models.Model):
    surname = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True)
    hobby = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.name

class ExpertBookRecomendation(models.Model):
    book_selection = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_selection')
    text = models.TextField()
    expert_selection = models.ForeignKey(ExpertBook, on_delete=models.CASCADE)

    def __str__(self):
        return f'эксперт: {self.expert_selection.name} книги: {self.book_selection.title}'