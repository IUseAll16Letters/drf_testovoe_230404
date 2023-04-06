import os
import time

from time import sleep
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')

app = Celery('service')
app.config_from_object('django.conf.settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task
def test_task():
    sleep(20)
    ret = ('*' * 5) + "Debug task done"
    return ret
