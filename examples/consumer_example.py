from confluent_kafka import Consumer, KafkaError

settings = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "mygroup",
    "client.id": "client-1",
    "enable.auto.commit": True,
    "session.timeout.ms": 6000,
    "default.topic.config": {"auto.offset.reset": "smallest"}
}

# Create Kafka Consumer
consumer = Consumer(settings)
consumer.subscribe(["weather"])

try:
    while True:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print(f"Received message: {msg.value()}")
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print(f"End of partition reached {msg.topic()}/{msg.partition()}")
        else:
            print(f"Error occured: {msg.error().str()}")

except KeyboardInterrupt:
    pass

finally:
    consumer.close()