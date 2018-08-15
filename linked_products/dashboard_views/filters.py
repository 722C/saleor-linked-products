from django.utils.translation import npgettext, pgettext_lazy
from django_filters import (CharFilter, OrderingFilter)

from saleor.core.filters import SortedFilterSet

from ..models import LinkedProduct

SORT_BY_FIELDS = {
    'name': pgettext_lazy('Linked product list sorting option', 'name')}


class LinkedProductFilter(SortedFilterSet):
    name = CharFilter(
        label=pgettext_lazy('Linked product list filter label', 'Name'),
        lookup_expr='icontains')
    sort_by = OrderingFilter(
        label=pgettext_lazy('Linked product list filter label', 'Sort by'),
        fields=SORT_BY_FIELDS.keys(),
        field_labels=SORT_BY_FIELDS)

    class Meta:
        model = LinkedProduct
        fields = []

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard linked products list',
            'Found %(counter)d matching linked product',
            'Found %(counter)d matching linked products',
            number=counter) % {'counter': counter}
