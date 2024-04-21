FROM python:3.11-slim-bullseye
COPY . /app
WORKDIR /app
RUN pip install google-cloud-aiplatform nicegui
CMD ["python3", "main.py"]
