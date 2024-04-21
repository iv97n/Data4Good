import logging
import os
from typing import Optional
import requests

from quixstreams import Application


# URL of the Flask API
api_url = 'http://127.0.0.1:5000/weather'


KAFKA_INPUT_TOPIC = 'sensor_topic'
KAFKA_OUTPUT_TOPIC = "feature_topic"
KAFKA_BROKER_ADDRESS = "localhost:9092"

weather_encoding = {
    "sunny": [1, 0, 0],
    "cloudy": [0, 1, 0],
    "rainy": [0, 0, 1]
}

# Define Quix your application and settings
app = Application(
    broker_address = KAFKA_BROKER_ADDRESS,
    consumer_group="json__users"
)

# Define an input topic with JSON deserializer
input_topic = app.topic(KAFKA_INPUT_TOPIC, value_deserializer="json")

# Make a GET request to the API
response = requests.get(api_url)
weather = response.json()['weather']
weather_encoded = weather_encoding[weather]

# Define an output topic with JSON serializer
output_topic = app.topic(KAFKA_OUTPUT_TOPIC, value_serializer="json")

# Create a StreamingDataFrame and start building your processing pipeline
sdf = app.dataframe(input_topic)

# Make a GET request to the API
response = requests.get(api_url)
weather = response.json()['weather']
weather_encoded = weather_encoding[weather]
sdf["weather"] = weather_encoded


# Send the message directly to the output topic without any transformation
sdf = sdf.to_topic(output_topic)

# Start message processing
app.run(sdf)
