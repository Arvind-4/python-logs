#!/bin/bash

APP_PORT=${PORT:-8000}

/opt/venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind "0.0.0.0:${APP_PORT}"