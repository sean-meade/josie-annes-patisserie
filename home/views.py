from django.shortcuts import render
from products.models import Product


# Create your views here.
def index(request):
    """ A view to return index page """
    products = Product.objects.all()[:4]

    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)
