from .celery import app as celery_app
celery_app.conf.broker_url = 'amqp://guest:guest@rabbitmq:5672/'
# celery_app.conf.broker_url = 'amqp://rabbitmq'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
# celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False # 
celery_app.conf.worker_prefetch_multiplier = 4
CELERY_TIMEZONE = 'Asia/Karachi'
