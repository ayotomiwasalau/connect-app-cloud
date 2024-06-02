FROM python:3.10-alpine

WORKDIR .

RUN apk update

RUN apk add --no-cache gcc musl-dev linux-headers libc-dev geos postgresql-dev

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]