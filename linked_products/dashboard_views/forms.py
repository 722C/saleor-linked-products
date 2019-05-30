from django import forms
from django.db.models import Q, Count
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category, Product
from ..models import LinkedProduct


class LinkedProductForm(forms.ModelForm):
    
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())

    class Meta:
        model = LinkedProduct
        verbose_name_plural = 'linked products'
        exclude = []

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance', None)
        if instance:
            self.fields['products'].queryset = Product.objects.annotate(link_count=Count('links')).filter(Q(link_count=0) | Q(links=instance))
        else:
            self.fields['products'].queryset = Product.objects.annotate(link_count=Count('links')).filter(link_count=0)


