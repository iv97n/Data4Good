from kafka import KafkaProducer
import json
import datetime
import random

# Initialize Kafka producer attached to a specific topic
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Specify the topic to which messages will be sent
topic = 'accidents_topic'

# Choose a random integer between 1000 and 50000
random_number = random.randint(1000, 50000)

# Choose a random sensor
random_id = random.randint(0, 190)

# Sample tabular data
sample = {"timestamp": datetime.datetime.now().isoformat(), "sensor_id": random_id, "number_of_vehicles": random_number}

# Serialize and send tabular data as JSON via Kafka
producer.send(topic, value=json.dumps(sample).encode('utf-8'))

# Flush the producer to ensure all messages are sent
producer.flush()

# Close the producer
producer.close()

