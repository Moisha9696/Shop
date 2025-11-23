from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_order_email(order, template_name, subject):
    """Отправка email о заказе"""
    context = {
        'order': order,
        'site_url': settings.SITE_URL,  # Добавьте в settings SITE_URL = 'http://yourdomain.com'
    }

    # Рендерим HTML шаблон
    html_content = render_to_string(f'emails/{template_name}', context)
    text_content = strip_tags(html_content)  # Создаем текстовую версию

    # Создаем email
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[order.email],
        cc=[settings.DEFAULT_FROM_EMAIL]  # Копия на администратора
    )
    email.attach_alternative(html_content, "text/html")

    try:
        email.send()
        return True
    except Exception as e:
        print(f"Ошибка отправки email: {e}")
        return False


def send_order_created_email(order):
    """Отправка email о создании заказа"""
    subject = f'Заказ #{order.id} успешно создан'
    return send_order_email(order, 'order_created.html', subject)


def send_order_status_email(order):
    """Отправка email об изменении статуса заказа"""
    status_display = order.get_status_display()
    subject = f'Статус заказа #{order.id} изменен на "{status_display}"'
    return send_order_email(order, 'order_status_changed.html', subject)


def send_admin_notification(order):
    """Уведомление администратора о новом заказе"""
    subject = f'Новый заказ #{order.id}'

    context = {
        'order': order,
        'site_url': settings.SITE_URL,
    }

    html_content = render_to_string('emails/admin_order_notification.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.ADMIN_EMAIL]  # Добавьте в settings ADMIN_EMAIL = 'admin@yourdomain.com'
    )
    email.attach_alternative(html_content, "text/html")

    try:
        email.send()
        return True
    except Exception as e:
        print(f"Ошибка отправки уведомления администратору: {e}")
        return False