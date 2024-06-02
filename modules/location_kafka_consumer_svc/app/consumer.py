
import psycopg2
import json
import os
from kafka import KafkaConsumer
from typing import Dict

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)

def insert_location_into_db(location):
    session = psycopg2.connect(dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)
    cursor = session.cursor()
    cursor.execute(
        'INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}));'.format(
            int(location["person_id"]), float(location["latitude"]), float(location["longitude"]))
        )
    session.commit()
    cursor.close()
    session.close()


    print("Location inserted to the database!")
    return location

for message in consumer:
    location = json.loads(message.value.decode("utf-8"))
    insert_location_into_db(location)