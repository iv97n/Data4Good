from kafka import KafkaProducer
import json
import datetime
import random

# Initialize Kafka producer attached to a specific topic
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Specify the topic to which messages will be sent
topic = 'accidents_topic'
accident_types = ["fatality", "serious", "minor"]

random_accident_type = random.choice(accident_types)
# Sample tabular data
sample = {"timestamp": datetime.datetime.now().isoformat(), "accident_type": random_accident_type}

# Serialize and send tabular data as JSON via Kafka
producer.send(topic, value=json.dumps(sample).encode('utf-8'))

# Flush the producer to ensure all messages are sent
producer.flush()

# Close the producer
producer.close()