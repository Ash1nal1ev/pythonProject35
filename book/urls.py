from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('book/',views.BookListView.as_view(), name='book_all'),
    # path('book/',views.book_all, name='book_all'),
    path('book/<int:id>/',views.BookDetailView.as_view(), name='book_detail'),
    # path('book/<int:id>/',views.book_detail, name='book_detail'),
    path('book/<int:id>/update/',views.BookUpdateView.as_view(), name="book_update"),
    # path('book/<int:id>/update/',views.book_update, name="book_update"),
    path('book/<int:id>/delete/',views.BookDeleteView.as_view(), name="book_delete"),
    # path('book/<int:id>/delete/',views.book_delete, name="book_delete"),
    path('book/<int:id>/raiting/',views.book_raiting, name="book_raiting"),
    path('add-book/',views.BookCreateView.as_view(), name='add-book'),
    # path('add-book/',views.add_book, name='add-book')
]