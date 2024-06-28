FROM python:3.10-slim-buster

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 cmake gcc g++  -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Set the default number of workers if not provided
ENV WORKERS=2

# Copy the entrypoint script
# COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script to run Uvicorn
ENTRYPOINT ["/app/entrypoint.sh"]