FROM python:3.10-alpine

WORKDIR .

RUN set -x \
    && apk update \
    && apk add build-base \
    && apk add linux-headers \
    && pip install --no-cache --upgrade pip setuptools \
    && pip install wheel
    
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5005

CMD ["python", "app/consumer.py"]