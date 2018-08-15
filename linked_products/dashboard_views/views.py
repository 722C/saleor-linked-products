from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy

from saleor.core.utils import get_paginator_items
from saleor.dashboard.views import staff_member_required
from .filters import LinkedProductFilter
from .forms import LinkedProductForm

from ..models import LinkedProduct


@staff_member_required
@permission_required('linked_products.view')
def linked_product_list(request):
    linked_products = (
        LinkedProduct.objects.all().order_by('name'))
    linked_product_filter = LinkedProductFilter(
        request.GET, queryset=linked_products)
    linked_products = get_paginator_items(
        linked_products, settings.DASHBOARD_PAGINATE_BY, request.GET.get('page'))
    # Call this so that cleaned_data exists on the filter_set
    linked_product_filter.form.is_valid()
    ctx = {
        'linked_products': linked_products, 'filter_set': linked_product_filter,
        'is_empty': not linked_product_filter.queryset.exists()}
    return TemplateResponse(request, 'linked_products/dashboard/list.html', ctx)


@staff_member_required
@permission_required('linked_products.edit')
def linked_product_create(request):
    linked_product = LinkedProduct()
    form = LinkedProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy('Dashboard message', 'Created linked product')
        messages.success(request, msg)
        return redirect('popular-category-dashboard-list')
    ctx = {'linked_product': linked_product, 'form': form}
    return TemplateResponse(request, 'linked_products/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('linked_products.edit')
def linked_product_details(request, pk):
    linked_product = LinkedProduct.objects.get(pk=pk)
    form = LinkedProductForm(
        request.POST or None, instance=linked_product)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated linked product %s') % linked_product.name
        messages.success(request, msg)
        return redirect('popular-category-dashboard-list')
    ctx = {'linked_product': linked_product, 'form': form}
    return TemplateResponse(request, 'linked_products/dashboard/detail.html', ctx)


@staff_member_required
@permission_required('linked_products.edit')
def linked_product_delete(request, pk):
    linked_product = get_object_or_404(LinkedProduct, pk=pk)
    if request.method == 'POST':
        linked_product.delete()
        msg = pgettext_lazy('Dashboard message',
                            'Removed linked product %s') % linked_product
        messages.success(request, msg)
        return redirect('popular-category-dashboard-list')
    return TemplateResponse(
        request, 'linked_products/dashboard/modal/confirm_delete.html', {'linked_product': linked_product})
