#!/bin/bash

# Start Kafka server in the background alongside zookeper
sudo /opt/zoekeeper/apache-zookeeper-3.8.4-bin/bin/zkServer.sh start &
sleep 5
sudo /opt/kafka/kafka-3.7.0-src/bin/kafka-server-start.sh /opt/kafka/kafka-3.7.0-src/config/server.properties &
sleep 5
sudo /opt/kafka/kafka-3.7.0-src/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic accidents_topic &
sleep 5
sudo /opt/kafka/kafka-3.7.0-src/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_topic &
sleep 5
sudo /opt/kafka/kafka-3.7.0-src/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic feature_topic &
sleep 5

# Start the weather api
python3 ./weather_api.py &
sleep 5

# Start each of the processes realted to the data engineering process
gnome-terminal --title="Model loader" -- bash -c "python3 /home/iv97n/Documents/Data4Good/src/./model_loader.py" 
python3 /home/iv97n/Documents/Data4Good/src/./accidents_etl.py &
python3 /home/iv97n/Documents/Data4Good/src/./sensor_etl.py &
# Detect 100 cars
for ((i=1; i<=100; i++))
do
    python3 /home/iv97n/Documents/Data4Good/src/./sensor_origin.py &
done

python3 /home/iv97n/Documents/Data4Good/src/./accidents_origin.py &
