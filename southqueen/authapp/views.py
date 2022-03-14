from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import messages

def login(request):
    title = 'вход'
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('products:index'))

    content = {'title': title, 'login_form': login_form}

    return render(request, 'authapp/login.html', context=content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))


def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            try:
                register_form.save()
                return HttpResponseRedirect(reverse('auth:login'))
            except:
                register_form.add_error(None, 'Ошибка регистрации')
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', context=content)


def edit(request):
    title = 'редактирование'
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', context=content)