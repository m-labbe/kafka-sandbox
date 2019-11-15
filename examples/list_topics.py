import click
from collections import namedtuple
from confluent_kafka.admin import AdminClient

Partition = namedtuple('Partition', ['id', 'leader', 'replicas', 'isrs', 'error'])

@click.command()
def main():
    admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})
    metadata = admin_client.list_topics()
    for topic in metadata.topics.items():
        print(topic)

if __name__ == "__main__":
    main()
