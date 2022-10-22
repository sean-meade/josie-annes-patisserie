from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    fdt = settings.FREE_DELIVERY_THRESHOLD

    if total < fdt:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = fdt - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

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
