from celery import shared_task
from django.core.mail import send_mail


@shared_task
def order_created(order_id):
    """
    Task to send an email notification when an order is successfully created
    """
    order = Order.objects.get(id=order_id)
    subject = f'Prder nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
        f'Your order nr. {order.id} has been successfully created.\n\n' \
        f'Best regards,\n\n' \
        f'Al-Syed'
        