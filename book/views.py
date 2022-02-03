from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.views import generic

class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()
    context_object_name = "post"

    def get_queryset(self):
        return models.Book.objects.filter().order_by("-id")

# def book_all(request):
#     post = models.Book.objects.all()
#     return render(request, "book_list.html", {'post': post})

class BookDetailView(generic.DetailView,generic.CreateView):
    template_name = "book_detail.html"
    context_object_name = 'book'


    def get_object(self, **kwargs):
        id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=id)

    form_class = forms.CommentForm
    queryset = models.BookComment.objects.all(), models.ExpertBookRecomendation.objects.all()
    success_url = "/book/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookDetailView, self).form_valid(form=form)

# def book_detail(request, id):
#     book = get_object_or_404(models.Book, id=id)
#     rate = models.Raiting.objects.filter(rait_id=id)
#     return render(request, 'book_detail.html', {'book': book,'rate':rate})

class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/book/"

# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('You add new book!')
#             return redirect(reverse("book:book_all"))
#     else:
#         form = forms.BookForm()
#     return render(request, "add_book.html", {"form": form})

class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/book/"

    def get_object(self, *kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)

# def book_update(request, id):
#     book_obj = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.BookForm(instance=book_obj, data=request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponse('book updated succefully')
#             return redirect(reverse("book:book_all"))
#     else:
#         form = forms.BookForm(instance=book_obj)
#     return render(request, 'book_update.html', {"form":form,'object': book_obj})

class BookDeleteView(generic.DeleteView):
    template_name = "book_delete.html"
    success_url = "/book/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return render(request,"book_delete.html")

# class BookRaitingView(generic.FormView):
#     template_name = "book_raiting.html"


def book_raiting(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    method = request.method
    if method == "POST":
        form = forms.RaitingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('You add new book!')
            return redirect(reverse("book:book_all"))
    else:
        form = forms.RaitingForm()
    return render(request, "book_raiting.html", {"form": form,'book':book_id})