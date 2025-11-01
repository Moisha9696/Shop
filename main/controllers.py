import logging
from .models import Category, Product

logger = logging.getLogger(__name__)

class CategoryController:
    @staticmethod
    def get_all():
        logger.info("Retrieving all categories ordered by name")
        return Category.objects.all().order_by('name')


class ProductController:
    @staticmethod
    def get_all():
        logger.info("Получение всех продуктов")
        return Product.objects.all().order_by('name')
