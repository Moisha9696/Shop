from .models import Order
import logging

logger = logging.getLogger(__name__)

def orders_count(request):
    logger.info(
        f"Получение количества заказов. Пользователь: {request.user}, Authenticated: {request.user.is_authenticated}")

    if not request.user.is_authenticated:
        logger.info(f"Получение количества заказов не авторизированного пользователя :: {request.session.session_key}")
        if request.session.session_key:
            orders_count = Order.objects.filter(session_key=request.session.session_key).count()
        else:
            orders_count = 0
        logger.info(f"Получение количества заказов не авторизированного пользователя: {orders_count}" )
        return {
            'orders_count': orders_count
        }
    if request.user.is_authenticated:
        logger.info("Получение количества заказов авторизированного пользователя")
        orders_count = Order.objects.filter(user=request.user).count()
        logger.info(f"Получение количества заказов авторизированного пользователя: {orders_count}" )
        return {
            'orders_count': orders_count
        }
    return {}