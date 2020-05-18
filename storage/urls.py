from . import views

from django.urls import path

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list_url"),
]
