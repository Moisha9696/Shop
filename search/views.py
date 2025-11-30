from django.shortcuts import render
from main.models import Product
from django.db.models import Q
from cart.forms import CartAddProductForm

def search_form_view(request):
    return render(request, 'search/search_form.html')


def search_results(request):
    query = request.GET.get('q')
    products = []
    cart_product_form = CartAddProductForm()

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'search/search_results.html', {
        'products': products,
        'query': query,
        'cart_product_form': cart_product_form
    })