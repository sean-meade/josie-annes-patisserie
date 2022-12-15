from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    delivery_item = False
    collection_item = False

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
        if str(product.category).lower() == 'delivery':
            delivery_item = True
        if str(product.category).lower() == 'collection':
            collection_item = True

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'collection_item': collection_item,
        'delivery_item': delivery_item,
    }

    return context
