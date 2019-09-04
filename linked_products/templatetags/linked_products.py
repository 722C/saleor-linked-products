from django import template

from saleor.product.utils import products_with_availability

register = template.Library()


@register.inclusion_tag('linked_products/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def linked_products_side_nav(context):
    return context


@register.inclusion_tag('linked_products/group.html', takes_context=True)
def linked_products(context, product):
    request = context.get('request', None)
    linked_product = product.links.first()
    context.update({
        'linked_product': linked_product
    })

    if linked_product and request:
        products = set()
        for p in product.links.all():
            products = products | set(filter(lambda product: product, p.products.all()))
        products = list(products)

        if len(products) > 1:
            longest_common_anchored_substring = ''
            for first, second in zip(products[0].name, products[1].name):
                if first == second:
                    longest_common_anchored_substring += first
                else:
                    break
            products_and_availability = list(products_with_availability(
                products, request.discounts, request.taxes,
                request.currency))
            context.update({
                'linked_product_products': products_and_availability,
                'linked_product_to_cut_from_name':
                longest_common_anchored_substring,
            })

    return context
