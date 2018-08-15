from django.db import models

from django.utils.translation import pgettext_lazy

from saleor.core.permissions import MODELS_PERMISSIONS


# Add in the permissions specific to our models.
MODELS_PERMISSIONS += [
    'linked_products.view',
    'linked_products.edit'
]


class LinkedProduct(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField('product.Product', related_name='links')
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'linked_products'

        permissions = (
            ('view', pgettext_lazy('Permission description',
                                   'Can view linked products')
             ),
            ('edit', pgettext_lazy('Permission description',
                                   'Can edit linked products')))

    def __str__(self):
        return self.name
