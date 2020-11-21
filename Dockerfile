FROM python:3.8-alpine3.11

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "-dutt", "main.py"]
