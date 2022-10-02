from django.shortcuts import render
from products.models import Product


def all_products(request):
    """ A view to show all products, including sorting search filtering """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

