from django import template

register = template.Library()


@register.inclusion_tag('linked_products/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def linked_products_side_nav(context):
    return context
