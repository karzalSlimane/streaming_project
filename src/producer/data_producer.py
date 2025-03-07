import random
import time
from kafka import KafkaProducer

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers=['kafka:9093'])

# List of locations to simulate data
locations = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

def generate_user_data():
    user_id = random.randint(1000, 9999)
    age = random.randint(18, 80)
    location = random.choice(locations)
    return {"user_id": user_id, "age": age, "location": location}

# Send data to Kafka every 1 second
while True:
    user_data = generate_user_data()
    producer.send('user-data', value=user_data)
    print(f"Sent: {user_data}")
    time.sleep(1)
