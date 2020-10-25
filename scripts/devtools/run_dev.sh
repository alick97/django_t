#!/bin/bash

echo "run celery worker..."
celery -A mysite.celery worker --loglevel INFO
