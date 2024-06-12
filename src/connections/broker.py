import os

from celery import Celery

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL")

celery_app = Celery("tasks", backend=CELERY_BACKEND_URL, broker=CELERY_BROKER_URL)
