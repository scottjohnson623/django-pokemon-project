#!/usr/bin/env bash

echo Starting Gunicorn.
exec gunicorn api.wsgi:application \
    --bind backend:8000 \
    --workers 1 \
    --chdir api
