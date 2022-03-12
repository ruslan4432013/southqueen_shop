from django.shortcuts import render


def main(request):
    context = {'title': 'главная'}
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {'title': 'продукты'}
    return render(request, 'mainapp/shop.html', context=context)


def contact(request):
    context = {'title': 'контакты'}
    return render(request, 'mainapp/contact.html', context=context)
