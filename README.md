# kafka-sandbox
Local environment for experimenting with Kafka

Resources:
* Setting up Docker containers:
  - https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html
* docker-compose.yml 
  - https://github.com/confluentinc/examples/blob/5.3.1-post/cp-all-in-one/docker-compose.yml
* Confluent Kafka Python Library 
  - https://github.com/confluentinc/confluent-kafka-python
  - https://docs.confluent.io/5.0.0/clients/confluent-kafka-python/
* Confluent quick-start guide for Python 
  - https://www.confluent.io/blog/introduction-to-apache-kafka-for-python-programmers/

Install dependencies
```
pipenv install
```

Build and start containers
```
docker-compose up -d --build
```

Create a topic
```
pipenv run python examples/create_topic.py mytopic
```

Kafka shell scripts
```
\\ Create a topic
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

\\ List topics
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181
```

