FROM python:3.11-slim-bullseye
COPY . /app
WORKDIR /app
RUN pip install google-cloud-aiplatform nicegui
RUN apt-get install apt-transport-https ca-certificates gnupg curl
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN apt-get update && sudo apt-get install google-cloud-cli
RUN gcloud init gcloud --no-launch-browser
CMD ["python3", "main.py"]
