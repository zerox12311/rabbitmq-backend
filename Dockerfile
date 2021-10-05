FROM python:3.9-alpine

WORKDIR /var/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind=0.0.0.0:8000", "main:app" ]