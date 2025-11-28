import logging
from .models import Category, Product

logger = logging.getLogger(__name__)

class CategoryController:
    @staticmethod
    def get_all():
        logger.info("Получение всех кателогий")
        return Category.objects.all().order_by('name')


class ProductController:
    @staticmethod
    def get_all():
        logger.info("Получение всех продуктов")
        return Product.objects.all().order_by('name')

    @staticmethod
    def get_by_category(category):
        logger.info("Получение всех продуктов для категории ")
        return Product.objects.filter(category=category).order_by('name')
