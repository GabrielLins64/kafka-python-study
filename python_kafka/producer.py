from kafka import KafkaProducer
import json


BOOTSTRAP_SERVER = 'localhost:9092'
TOPIC = 'my-topic-name'

json_value_serializer = lambda m : str.encode(json.dumps(m))

def send_text_message(producer: KafkaProducer, topic: str, message: str):
    # Block until a single message is sent (or timeout)
    future = producer.send(topic, str.encode(message))
    result = future.get(timeout=60)

def send_many_messages(producer: KafkaProducer, topic: str, messages: list[str]):
    for message in messages:
        producer.send(topic, str.encode(message))

    # Block until all pending messages are at least put on the network
    # NOTE: This does not guarantee delivery or success! It is really
    # only useful if you configure internal batching using linger_ms
    producer.flush()

def send_json_message(producer: KafkaProducer, topic: str, message_json: dict):
    # Use a key for hashed-partitioning
    future = producer.send(topic, key=b'foo', value=json_value_serializer(message_json))
    result = future.get(timeout=60)


if __name__ == '__main__':
    # create a producer. broker is running on localhost
    producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER])

    # Send a single message
    send_text_message(producer, TOPIC, "Minha mensagem")

    # Send many messages
    # messages = []
    # for _ in range(100):
    #     messages.append("Some text message")
    # send_many_messages(producer, TOPIC, messages)

    # Send json message
    # json_message = {
    #     'key1': 'bar1',
    #     'key2': 'bar2',
    # }
    # send_json_message(producer, TOPIC, json_message)
    