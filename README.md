# saleor-linked-products

Linked Products Plugin for [Saleor](https://github.com/mirumee/saleor)

This provides a (currently skeleton) implementation of linked products. This is currently built for the `v2018.6` tag of Saleor.

Adding the linked products as a separate model allows for additional fields to be added specific to the relationship.

---

## Installation

To install, `pip install` the package as such:

```bash
pip install git+git://github.com/722c/saleor-linked-products.git#egg='saleor-linked-products'
```

Or list the package in your `requirements.txt` as such:

```
git+git://github.com/722c/saleor-linked-products.git#egg='saleor-linked-products'
```

Alternatively, this can be installed as a Git submodule directly in the root directory of your Saleor instance.

## Configuration

Once you have installed the app, you will need to add a few things to your project:

Add the app to your installed apps (the order doesn't matter):

```python
INSTALLED_APPS = [
    ...

    # Saleor plugins
    'saleor-linked-products.linked_products',

    ...
]
```

Add the apps URLs to your root `urls.py` in the `translatable_urlpatterns` near the bottom (this will allow any native Saleor URLs to be matched beforehand):

```python
translatable_urlpatterns = [
    ...
    url(r'^search/', include((search_urls, 'search'), namespace='search')),

    # URLs for saleor-linked-products
    url(r'', include('saleor-linked-products.linked_products.urls')),

    url(r'', include('payments.urls'))
]
```

Finally, add the link to the dashboard by importing the template tag in `templates/dashboard/base.html` and putting it where you want in the side nav:

```django
<!DOCTYPE html>
{% load staticfiles i18n %}
 ...

 <!-- This is template tag you will need to load. -->
{% load linked_products_side_nav from linked_products %}

...

<ul class="side-nav">
  <li class="nav-home">
    <a href="{% url 'dashboard:index' %}">
      {% trans "Home" context "Dashboard homepage" %}
    </a>
  </li>
  {% if perms.product.view_product or perms.product.view_category %}
  <li class="side-nav-section" id="first">
    ...
  </li>
  {% endif %}

  <!-- Add in the saleor-linked-products where you want. -->
  {% linked_products_side_nav %}

  ...
</ul>

...
```
