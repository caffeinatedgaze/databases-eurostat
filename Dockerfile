FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY ./app /app

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]