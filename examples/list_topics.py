import click
from collections import namedtuple
from confluent_kafka.admin import AdminClient

Partition = namedtuple('Partition', ['id', 'leader', 'replicas', 'isrs', 'error'])

@click.command()
def main():
    admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})
    metadata = admin_client.list_topics()
    topics = {}
    for topic, meta in metadata.topics.items():
        print(meta)
        topics[topic] = [Partition(partition_id, partition.leader, sorted(partition.replicas), sorted(partition.isrs), partition.error) for partition_id, partition in sorted(meta.partitions.items())]

if __name__ == "__main__":
    main()
