import math
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    individual_dessert_count = 0

    for item_id, item_data in bag.items():

        if isinstance(item_data, int):

            product = get_object_or_404(Product, pk=item_id)
            if product.individual_dessert:
                individual_dessert_count += item_data
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'price': product.price,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            if product.individual_dessert:
                individual_dessert_count += item_data
            for size, quantity in item_data['items_by_size'].items():
                if size == 'm':
                    total += quantity * product.medium_price
                    price = product.medium_price
                elif size == 'l':
                    total += quantity * product.large_price
                    price = product.large_price
                else:
                    total += quantity * product.price
                    price = product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price': price,
                })

    desert_discount = 0
    if individual_dessert_count / 6 > 0:
        desert_discount = 2.00 * math.floor(individual_dessert_count / 6)
        if individual_dessert_count % 6 > 3:
            desert_discount += 1.50 * (individual_dessert_count % 6) / 4
    elif individual_dessert_count / 4 > 0:
        desert_discount = 1.50 * math.floor(individual_dessert_count / 4)

    grand_total = round(float(total), 2) - desert_discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'desert_discount': desert_discount,
    }

    return context
