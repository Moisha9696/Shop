from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
# from .tasks import order_created
from cart.cart import Cart, logger


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():

            # Убеждаемся, что сессия существует
            if not request.session.session_key:
                logger.info("создание сессии")
                request.session.create()
            else:
                logger.info("сессия уже существует")

            order = form.save(commit=False)

            # Сохраняем данные сессии
            if not request.user.is_authenticated:
                logger.info("Сохраняем данные сессии")
                order.session_key = request.session.session_key

            # Сохраняем user_id если пользователь залогинен
            if request.user.is_authenticated:
                logger.info("Сохраняем user_id если пользователь залогинен")
                order.user = request.user

            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


def order_list(request):
    # Для неавторизованных пользователей
    if not request.user.is_authenticated:
        # Получаем заказы по session_key текущей сессии
        session_key = request.session.session_key

        if not session_key:
            # Если сессии нет, показываем пустой список
            orders = Order.objects.none()
        else:
            # Ищем заказы по session_key
            orders = Order.objects.filter(session_key=session_key)

        context = {
            'orders': orders,
            'is_authenticated': False
        }

        return render(request, 'orders/order/order_list.html', context)

    # Для авторизованных пользователей (если нужно)
    else:
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders': orders,
            'is_authenticated': True
        }
        return render(request, 'orders/order/order_list.html', context)


def order_detail(request, order_id):
    try:
        # Получаем заказ
        order = get_object_or_404(Order, id=order_id)

        # Проверяем права доступа
        if request.user.is_authenticated:
            # Для авторизованных - только свои заказы
            if order.user != request.user:
                return HttpResponseForbidden("У вас нет доступа к этому заказу")
        else:
            # Для неавторизованных - только заказы их сессии
            if order.session_key != request.session.session_key:
                return HttpResponseForbidden("У вас нет доступа к этому заказу")

        # Получаем товары заказа
        order_items = order.items.all()  # предполагается, что есть related_name='items'

        context = {
            'order': order,
            'order_items': order_items,
        }

        return render(request, 'orders/order/order_detail.html', context)

    except Order.DoesNotExist:
        raise Http404("Заказ не найден")