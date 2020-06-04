from django.http import HttpResponseRedirect, JsonResponse
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

    return save_good_form(request, form, 'mainapp/create.html')
    # return render(request, 'mainapp/create.html', content)


def save_good_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            goods = Product.objects.all()
            data['html_good_list'] = render_to_string('good_list.html', {
                'goods': goods
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
