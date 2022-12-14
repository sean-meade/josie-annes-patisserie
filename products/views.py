from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from products.forms import ProductForm
from products.models import Product, Category, Allergens


def all_products(request, category, page):
    """ A view to show all products, including sorting search filtering """

    products = Product.objects.filter(category__friendly_name=category)
    query = None
    # sort = None
    direction = None
    allergens_checked = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if direction in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET.get('q', '')

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query)
            products = products.filter(queries)

        if 'allergens' in request.GET:
            allergens_checked = request.GET.getlist('allergens')

            products = products.exclude(allergens__allergy__in=allergens_checked)

        if not query and not allergens_checked and 'q' not in request.GET:
            messages.error(request, "You didn't enter anything to search")

    all_allergens = ["gluten", "egg", "celery", "nut", "mustard", "soy", "milk", "sesame seed"]

    if query is None and allergens_checked is None:
        if category == 'collection':
            messages.info(request, f"These items need to be collected in store.")
        if category == 'delivery':
            messages.info(request, f"These items can be delivered within Ireland.")

    paginator = Paginator(products, per_page=3)
    page_object = paginator.get_page(page)

    context = {
        'products': products,
        'search_term': query,
        'exclude_allergens': allergens_checked,
        'all_allergens': all_allergens,
        'current_category': category,
        "page_obj": page_object,
    }

    return render(request, 'products/products.html', context)


def find_product(request, sku):
    product = get_object_or_404(Product, sku=sku)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Successfully added product!')
                return redirect(reverse('product_detail', args=[product.sku]))
            else:
                messages.error(request, 'Failed to add product. Please ensure the form is valid.')
        except Exception:
            messages.error(request, f"An Error occurred, please try reducing the file size of the image and try again."
                                    f"Max size is 10MB.")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def edit_product(request, sku):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, sku=sku)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.sku]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, sku):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, sku=sku)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def choice(request):
    return render(request, 'products/store_choice.html')
