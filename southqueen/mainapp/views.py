from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    context = {'title': 'главная'}
    return render(request, 'mainapp/index.html', context=context)


def products(request, pk=None):
    products = Product.objects.all()[:18]
    categories = ProductCategory.objects.all()

    context = {'title': 'продукты',
               'products': products,
               'categories': categories}
    return render(request, 'mainapp/shop.html', context=context)


def contact(request):
    context = {'title': 'контакты'}
    return render(request, 'mainapp/contact.html', context=context)
