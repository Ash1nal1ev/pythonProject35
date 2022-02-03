from django.urls import path
from . import views

app_name = "fabrics"
urlpatterns = [
    path("electronics/", views.ElectronicsProductListView.as_view(), name="product_list"),
    path("adidas/", views.AdidasProductListView.as_view(), name="product_list"),
    path("nike/", views.NikeProductListView.as_view(), name="product_list"),
    path("geek/", views.GeekProductListView.as_view(), name="product_list"),
    path("add-fabrics/", views.OrderCreateView.as_view(), name="order_create"),
    path("fabrics/<int:id>/", views.ProductDetailView.as_view(),name="cloth_detail"),
]