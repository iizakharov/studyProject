from django.http import HttpResponseRedirect
from django.shortcuts import render

from mainapp.forms import ProductForm
from mainapp.models import Product


def main(request):

    content = {
        'title': 'Главная',
        'products': Product.objects.filter(is_active=True),
    }

    return render(request, 'mainapp/index.html', content)


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    content = {
        'title': 'Добавление товара',
        'form': form,
    }

    return render(request, 'mainapp/create.html', content)
