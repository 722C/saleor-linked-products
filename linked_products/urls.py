from django.conf.urls import url

from .dashboard_views import views as dashboard_views

urlpatterns = [
    url(r'^dashboard/linked-products/$',
        dashboard_views.linked_product_list,
        name='linked-product-dashboard-list'),
    url(r'^dashboard/linked-products/create/$',
        dashboard_views.linked_product_create,
        name='linked-product-dashboard-create'),
    url(r'^dashboard/linked-products/(?P<pk>[0-9]+)/$',
        dashboard_views.linked_product_details,
        name='linked-product-dashboard-detail'),
    url(r'^dashboard/linked-products/(?P<pk>[0-9]+)/delete/$',
        dashboard_views.linked_product_delete,
        name='linked-product-dashboard-delete'),
]
