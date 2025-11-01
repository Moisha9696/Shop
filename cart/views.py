import logging

from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm
from main.models import Product

logger = logging.getLogger(__name__)

@require_POST
def cart_add(request, product_id):
    logging.info("cart_add")
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    logging.info(f"Добавляем в конзину продукт {product}")
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        logging.info("IS_VALID")
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    else:
        logging.info("NOT IS_VALID")
        logger.info(form.errors)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
