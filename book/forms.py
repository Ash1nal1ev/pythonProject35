from dataclasses import field
from pyexpat import model
from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"

class RaitingForm(forms.ModelForm):
    class Meta:
        model = models.Raiting
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.BookComment
        fields = "__all__"