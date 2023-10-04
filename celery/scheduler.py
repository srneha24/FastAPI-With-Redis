import requests
import logging
from celery import Celery

from env_vars import FASTAPI_IP

app = Celery('scheduler')
app.config_from_object('config')


@app.task
def increment_value():
    response = requests.post(url=f"http://{FASTAPI_IP}:8000/redis/first")

    logging.info("Task Has Been Triggered")

    return response.json()
