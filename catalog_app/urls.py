from django.urls import path
from . import views
from catalog_app.apps import CatalogAppConfig
app_name = CatalogAppConfig.name
urlpatterns = [
    path('', views.home, name='home'),                  # http://127.0.0.1:8000
    path('contacts/', views.contact, name='contact'),  # http://127.0.0.1:8000/contact/
    path('catalog/', views.products_list, name='products_list'),     # http://127.0.0.1:8000/product/
    path('catalog/<int:pk>/', views.product_detail, name='product_detail')
]