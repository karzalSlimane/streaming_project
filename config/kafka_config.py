from kafka import KafkaProducer
import json

# Define Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['kafka:9093'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define the Kafka topic
TOPIC = 'user-data'

def send_message(message):
    producer.send(TOPIC, message)
    producer.flush()
    print(f"Sent message: {message}")
