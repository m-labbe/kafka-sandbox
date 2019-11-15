# kafka-sandbox
Local environment for experimenting with Kafka

### Resources
* Setting up Docker containers
  - https://docs.confluent.io/current/quickstart/ce-docker-quickstart.html
* Example docker-compose.yml
  - https://github.com/confluentinc/examples/blob/5.3.1-post/cp-all-in-one/docker-compose.yml
* Access Kafka from outside Docker
  - https://rmoff.net/2018/08/02/kafka-listeners-explained/
  - https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc
* Confluent Kafka Python Library 
  - https://github.com/confluentinc/confluent-kafka-python
  - https://docs.confluent.io/5.0.0/clients/confluent-kafka-python/
* Confluent quick-start guide for Python 
  - https://www.confluent.io/blog/introduction-to-apache-kafka-for-python-programmers/

## Project setup

Install dependencies
```
pipenv install
```

Build and start containers
```
docker-compose up -d --build
```

## Producing and Consuming from the command line

Create a topic
```
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic mytopic
```

List topics
```
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181
```

Delete a topic
```
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic mytopic
```

Create a Producer
```
docker exec -it kafka /opt/kafka/bin/kafka-console-producer.sh --broker-list kafka:9092 --topic mytopic
```

Create a Consumer
```
docker exec -it kafka /opt/kafka/bin/kafka-console-consumer.sh --from-beginning --bootstrap-server kafka:9092 --topic mytopic
```

## Producing and Consuming from Python

Create a Topic
```
pipenv run python examples/create_topic.py mytopic
```

List Topics
```
pipenv run python examples/list_topics.py
```

Create a Producer and generate messages

```
pipenv run python examples/producer_example.py
```

Create a Consumer
```
pipenv run python examples/consumer_example.py
```








