from . import views

from django.urls import path

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list_url"),
    path("product-add/", views.ProductAddView.as_view(), name="product_add_url"),
    path("product/<str:vendor_code>/", views.ProductDetailView.as_view(), name="product_detail_url"),
    path("product/delete/<str:vendor_code>/", views.ProductDeleteView.as_view(), name="product_delete_url"),
]
