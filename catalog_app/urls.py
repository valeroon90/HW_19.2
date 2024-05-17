from django.urls import path
from . import views
from catalog_app.apps import CatalogAppConfig
app_name = CatalogAppConfig.name
urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contact'),
    path('products/', views.products_list, name='products_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail')
]