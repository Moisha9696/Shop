import logging

from django.shortcuts import render
from django.views.generic import ListView

from .controllers import ProductController

logger = logging.getLogger(__name__)

def all_list(request):
    products = ProductController.get_all()
    logger.info("Получение всех продуктов")
    for product in products:
        logger.info(product)
    return render(request, 'main/index/index.html',{'products': products})

