from .models import Order
import logging

logger = logging.getLogger(__name__)

def orders_count(request):
    logger.info(
        f"Получение количества заказов. Пользователь: {request.user}, Authenticated: {request.user.is_authenticated}")

    if not request.user.is_authenticated:
        logger.info("Получение количества заказов не авторизированного пользователя")
        return {
            'orders_count': Order.objects.filter(session_key=request.session.session_key)
        }
    if request.user.is_authenticated:
        logger.info("Получение количества заказов авторизированного пользователя")
        return {
            'orders_count': Order.objects.filter(user=request.user)
        }
    return {}