from django.shortcuts import render

from mainapp.models import Product


def main(request):

    content = {
        'title': 'Главная',
        'products': Product.objects.filter(is_active=True),
    }

    return render(request, 'mainapp/index.html', content)
