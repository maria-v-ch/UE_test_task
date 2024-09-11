from django.urls import path
from .views import ProductTariffView


urlpatterns = [
    path('products-tariffs', ProductTariffView.as_view(), name='product-tariffs'),
]
