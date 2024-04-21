# Consumer Script (consumer.py)
from kafka import KafkaConsumer

consumer = KafkaConsumer("feature_topic", bootstrap_servers='localhost:9092', group_id='my-group')

# Continuously listen for messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")

# Close the consumer
consumer.close()