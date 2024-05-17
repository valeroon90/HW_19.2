from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from catalog_app.models import Product


def home(request):
   #t = render_to_string('catalog_app/home.html')
   #return HttpResponse(t)
   context = {
       'title': 'Онлайн магазин "Натур-продукт"'
   }
   return render(request, 'catalog_app/home.html', context)


def contact(request):
    if request.method == 'POST':
      name = request.POST.get('name')
      phone = request.POST.get('phone')
      message = request.POST.get('message')
      print(f'You have new message from {name}({phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog_app/contact.html', context)




def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Список продуктов'
    }
    return render(request, 'catalog_app/products_list.html', context)


def product_detail(request, pk):
    product_ = Product.objects.get(pk=pk)
    context = {'product': product_}
    return render(request, "catalog_app/product_detail.html", context)






