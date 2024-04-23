from django.contrib import admin
from catalog_app.models import Product, Category
# Register your models here.
#admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
#admin.site.register(Product)
#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
 #   list_display = ('first_name', 'last_name',)
 #   list_filter = ('is_active',)
  #  search_fields = ('first_name', 'last_name',)
