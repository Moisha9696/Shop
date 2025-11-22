import logging

from django.shortcuts import render,  get_object_or_404

from cart.forms import CartAddProductForm
from .controllers import CategoryController, ProductController
from .models import Category

logger = logging.getLogger(__name__)

def all_list(request):
    products = ProductController.get_all()
    categories = CategoryController.get_all()
    cart_product_form = CartAddProductForm()
    return render(request,
                  'main/index/index.html',
                  {
                      'products': products,
                      'categories': categories,
                      'cart_product_form': cart_product_form
                  })

def product_list(request, category_slug):
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    products = ProductController.get_by_category(category)
    categories = CategoryController.get_all()
    cart_product_form = CartAddProductForm()
    return render(request,
                  'main/index/index.html',
                  {
                      'category': category,
                      'products': products,
                      'categories': categories,
                      'cart_product_form': cart_product_form
                  })

def product_detail(request):
    products = ProductController.get_all()
    categories = CategoryController.get_all()
    cart_product_form = CartAddProductForm()
    return render(request,
                  'main/index/index.html',
                  {
                      'products': products,
                      'categories': categories,
                      'cart_product_form': cart_product_form
                  })
