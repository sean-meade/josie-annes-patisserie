from django.shortcuts import render, get_object_or_404
from products.models import Product


def all_products(request):
    """ A view to show all products, including sorting search filtering """

    products = Product.objects.all()



    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def find_product(request, sku):

    product = get_object_or_404(Product, sku=sku)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
