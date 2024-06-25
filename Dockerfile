FROM python:3.10-slim-buster

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 cmake gcc g++  -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Ensure the virtual environment is used by uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8111"]
