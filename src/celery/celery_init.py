from celery import Celery

CELERY_BROKER = "amqp://guest:guest@rabbitmq3:5672/"
CELERY_BACKEND = "redis://redis:6379/0"

celery = Celery("tasks", broker=CELERY_BROKER, backend=CELERY_BACKEND)

celery.conf.update(
    {
        "broker_connection_retry": True,
        "broker_connection_retry_on_startup": True,
    }
)
