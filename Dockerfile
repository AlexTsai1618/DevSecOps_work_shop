FROM python:3.7.3-alpine

WORKDIR /app

COPY ./django.nV/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./django.nv /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

