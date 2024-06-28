#!/bin/sh

# Default to 1 worker if WORKERS is not set or empty
WORKERS=${WORKERS:-1}

# Start Uvicorn with the specified number of workers
exec uvicorn main:app --host 0.0.0.0 --port 8111 --workers $WORKERS
