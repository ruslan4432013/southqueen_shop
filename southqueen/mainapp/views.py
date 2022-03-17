from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {'title': 'главная',
               'basket': basket,
               'links_menu': links_menu}
    return render(request, 'mainapp/index.html', context=context)


def products(request, pk=None):

    links_menu = ProductCategory.objects.all()
    title = 'Продукты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 'all':
            category = {"name": "Все"}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
            title = category.name
        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket
        }

        return render(request, 'mainapp/shop-list.html', context=context)

    some_products = Product.objects.all()

    context = {'title': title,
               'basket': basket,
               'some_products': some_products,
               'links_menu': links_menu}
    return render(request, 'mainapp/shop.html', context=context)


def contact(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    links_menu = ProductCategory.objects.all()
    context = {'title': 'контакты',
               'basket': basket,
               'links_menu': links_menu}
    return render(request, 'mainapp/contact.html', context=context)
