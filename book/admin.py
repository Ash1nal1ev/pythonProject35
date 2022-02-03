from django.contrib import admin
from . import models

admin.site.register(models.Book)
admin.site.register(models.Raiting)
admin.site.register(models.BookComment)
admin.site.register(models.ExpertBook)
admin.site.register(models.ExpertBookRecomendation)