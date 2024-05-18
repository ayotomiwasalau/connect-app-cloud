FROM python:3.10-alpine

WORKDIR .

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5005

CMD ['python', 'app/consumer.py']