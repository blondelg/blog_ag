FROM python:3.8-alpine
RUN pip install --upgrade pip 
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && pip install pytz \
    && pip install backports.zoneinfo \
    && apk del build-deps
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000  
CMD python manage.py runserver 0.0.0.0:8000
