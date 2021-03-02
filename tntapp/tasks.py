from django.conf import settings
from celery import shared_task
from .models import Order


@shared_task

def new_order(name, phone):

	order_item= Order.objects.create(name=name, phone= phone)
    
    