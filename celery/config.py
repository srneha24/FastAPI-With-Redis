from datetime import timedelta

from env_vars import REDIS_IP

broker_url = f'redis://{REDIS_IP}:6379/0'
result_backend = f'redis://{REDIS_IP}:6379/0'
task_serializer = 'json'
result_serializer = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'UTC'

CELERY_BEAT_SCHEDULE = {
    'run-every-15-seconds': {
        'task': 'scheduler.increment_value',
        'schedule': timedelta(seconds=15),
    },
}