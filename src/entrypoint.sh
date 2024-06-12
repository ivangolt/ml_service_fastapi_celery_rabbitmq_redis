#!/bin/bash

# Check if the APP_MODE environment variable is defined
if [ -z "$APP_MODE" ]; then
    echo "ERROR: The APP_MODE environment variable is not defined."
    exit 1
fi

# Launching the App or Worker corresponding
if [ "$APP_MODE" = "worker" ]; then
    poetry run celery -A src.celery.worker.celery worker --loglevel=info --logfile=/logs/celery.log
elif [ "$APP_MODE" = "app" ]; then
    poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000
else
    echo "ERROR: Invalid value of the APP_MODE environment variable, 'app' or 'worker' is expected."
    exit 1
fi