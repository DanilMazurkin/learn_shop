from django.http import Http404
from django.shortcuts import render
from products_category.models import Product, Category


def index(request):
    sort_param = request.GET.get('sort', None)

    if sort_param == 'price':
        products = Product.objects.order_by('price')
    elif sort_param == '-price':
        products = Product.objects.order_by('-price')

    return render(request, "products.html", context={'products': products})


def product(request, id_product):
    try:
        product = Product.objects.get(pk=id_product)
    except Product.DoesNotExist:
        raise Http404("No MyModel matches the given query.")

    return render(request, "product.html", context={'product': product})


def categories(request):
    categories = Category.objects.all()

    return render(request, "categories.html", context={'categories': categories})
