from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductListView(ListView):
    queryset = models.ProductCL.objects.order_by("-id")
    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.order_by("-id")


class ProductDetailView(DetailView):
    template_name = "cloth_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=product_id)


class OrderCreateView(CreateView):
    template_name = "add-cloth.html"
    form_class = forms.OrderForm
    success_url = "/fabrics/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)


class ElectronicsProductListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Electronics").order_by("-id")
    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Electronics").order_by("-id")

class AdidasProductListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Adidas").order_by("-id")
    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Adidas").order_by("-id")

class NikeProductListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Nike").order_by("-id")
    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Nike").order_by("-id")

class GeekProductListView(ListView):
    queryset = models.ProductCL.objects.filter(
        tags__name="Geek").order_by("-id")
    template_name = "cloth_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(
            tags__name="Geek").order_by("-id")