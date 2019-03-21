import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

celery = Celery('tasks')
celery.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
celery.autodiscover_tasks()
