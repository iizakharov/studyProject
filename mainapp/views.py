from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from mainapp.forms import ProductForm
from mainapp.models import Product


def main(request):
    content = {
        'title': 'Главная',
        'products': Product.objects.filter(is_active=True),
    }
    return render(request, 'mainapp/index.html', content)


def create(request):
    data = dict()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['products_html'] = render_to_string('mainapp/product_list.html',
                                                     {'products': products})
        else:
            data['form_html'] = render_to_string('mainapp/includes/form.html',
                                                 {'form': form},
                                                 request=request)
    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('mainapp/includes/form.html',
                                             {'form': ProductForm()},
                                             request=request)

    return JsonResponse(data)
