from datetime import timedelta

from env_vars import REDIS_IP

broker_url = f'redis://{REDIS_IP}:6379/0'
result_backend = f'redis://{REDIS_IP}:6379/0'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'

beat_schedule = {
    'run-every-15-seconds': {
        'task': 'scheduler.increment_value',
        'schedule': timedelta(seconds=15),
    },
}
