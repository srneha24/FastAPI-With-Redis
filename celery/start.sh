#!/bin/sh
celery -A scheduler worker --loglevel=info &
celery -A scheduler beat --loglevel=info
