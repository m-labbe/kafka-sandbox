from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {0}: {1}")
    else:
        print(f"Message produced: {0}")

p = Producer({'bootstrap.servers': 'localhost:9092'})

try:
    for val in range(1, 1000):
        p.produce('mytopic', 'myvalue #{0}', callback=acked)
        p.poll(0.5)
except KeyboardInterrupt:
    pass

p.flush(30)
