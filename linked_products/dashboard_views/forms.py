from django import forms
from django.db.models import Q
from django.utils.translation import pgettext_lazy

from saleor.product.models import Category, Product
from ..models import LinkedProduct

from django.urls import reverse_lazy
from saleor.dashboard.forms import AjaxSelect2MultipleChoiceField

class LinkedProductForm(forms.ModelForm):
    products = AjaxSelect2MultipleChoiceField(
        queryset=Product.objects.all(),
        fetch_data_url=reverse_lazy('dashboard:ajax-products'), required=False)

    class Meta:
        model = LinkedProduct
        verbose_name_plural = 'linked products'
        exclude = []
