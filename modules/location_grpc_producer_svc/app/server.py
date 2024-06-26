import grpc
import location_pb2
import location_pb2_grpc
import time
import json
import os
from kafka import KafkaProducer
from concurrent import futures


TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Running...")
        request_value = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
        }
        user_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(TOPIC_NAME, user_encode_data)
        producer.flush()
        print(request_value)
        return location_pb2.LocationMessage(**request_value)
    
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

