from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    is_delivery = False

    fdt = settings.FREE_DELIVERY_THRESHOLD

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        if product.category == 'delivery':
            is_delivery = True

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < fdt:
        delivery = round(total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100))
        free_delivery_delta = fdt - total
    else:
        delivery = 0
        free_delivery_delta = 0

    if is_delivery:
        grand_total = delivery + total
    else:
        grand_total = total
        delivery = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': fdt,
        'grand_total': grand_total,
    }

    return context
