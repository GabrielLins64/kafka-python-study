from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


SERVER_HOST = "localhost"
SERVER_PORT = "9092"
KAFKA_TOPIC = "notification-system-local-tests"


def value_serializer(m): return json.dumps(m).encode('utf-8')


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=[f'{SERVER_HOST}:{SERVER_PORT}'],
        value_serializer=value_serializer)

    with open("notification.json") as f:
        data = json.load(f)

    payload = {
        "message": data['message'],
        "metadata": data['metadata'],
        "recipients": data['recipients'],
        "senderSystem": data['senderSystem'],
        "broadcast": data['broadcast']
    }

    future = producer.send(KAFKA_TOPIC, payload)

    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
        print("Message successfully sent!")
        print(f"topic: {record_metadata.topic}")
        print(f"partition: {record_metadata.partition}")
        print(f"offset: {record_metadata.offset}")

    except KafkaError:
        print("Message failed!")
