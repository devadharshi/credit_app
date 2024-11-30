from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'credit_approval_system.settings')

app = Celery('credit_approval_system')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related config keys should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
