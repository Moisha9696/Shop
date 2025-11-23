from .models import Order


class SessionOrderManager:
    """Менеджер для работы с заказами по сессии"""

    @staticmethod
    def get_session_orders(session_key):
        """Получить все заказы по ключу сессии"""
        return Order.objects.filter(session_key=session_key).order_by('-created_at')

    @staticmethod
    def get_session_order(session_key, order_id):
        """Получить конкретный заказ по сессии"""
        try:
            return Order.objects.get(id=order_id, session_key=session_key)
        except Order.DoesNotExist:
            return None

    @staticmethod
    def create_session_order(session_key, order_data, cart_items):
        """Создать заказ для сессии"""
        from decimal import Decimal

        # Создаем заказ
        order = Order.objects.create(
            session_key=session_key,
            **order_data
        )

        # # Создаем элементы заказа
        # for item_data in cart_items:
        #     order.items.create(
        #         product_name=item_data['name'],
        #         price=Decimal(item_data['price']),
        #         quantity=item_data['quantity']
        #     )

        return order

    @staticmethod
    def merge_session_orders(session_key, user, email):
        """Объединить заказы сессии с аккаунтом пользователя"""
        orders = Order.objects.filter(
            session_key=session_key,
            user__isnull=True
        )

        updated_count = orders.update(
            user=user,
            email=email  # Обновляем email на тот, что у пользователя
        )

        return updated_count