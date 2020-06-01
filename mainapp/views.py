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

    content = {
        'title': 'Добавление товара',
        'form': ProductForm,
    }

    return render(request, 'mainapp/create.html', content)