import click

from confluent_kafka.admin import AdminClient, NewTopic
admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})

@click.command()
@click.argument("topic_name")
@click.option("--partitions", default=1)
@click.option("--replication", default=1)
def main(topic_name, partitions, replication):
    topic_list = []
    topic_list.append(NewTopic(topic_name, partitions, replication))
    print(topic_list)
    admin_client.create_topics(topic_list)

if __name__ == "__main__":
    main()
