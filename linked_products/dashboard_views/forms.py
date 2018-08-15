from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category
from ..models import LinkedProduct


class LinkedProductForm(forms.ModelForm):

    class Meta:
        model = LinkedProduct
        verbose_name_plural = 'linked products'
        exclude = []
