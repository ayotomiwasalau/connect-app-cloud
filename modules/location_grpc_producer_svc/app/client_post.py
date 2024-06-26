import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    longitude=30.6,
    latitude=45.7,
)

response = stub.Create(location)
