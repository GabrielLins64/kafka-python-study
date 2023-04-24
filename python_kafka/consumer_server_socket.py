from kafka import KafkaConsumer
import socketio
import json


BOOTSTRAP_SERVER = 'localhost:9092'
TOPIC = 'my-topic-name'
GROUP_ID = 'my-group-2'


def create_consumer() -> KafkaConsumer:
    json_value_deserializer = lambda m : json.loads(m.decode('utf-8'))
    str_value_deserializer = lambda m : m.decode('utf-8')

    consumer = KafkaConsumer(TOPIC,
                            group_id=GROUP_ID,
                            bootstrap_servers=[BOOTSTRAP_SERVER],
                            value_deserializer=str_value_deserializer)
                            #  value_deserializer=json_value_deserializer)
    return consumer


def create_socket_server():
    sio = socketio.AsyncServer()
    app = socketio.ASGIApp(sio)

    @sio.event
    def connect(sid, environ):
        print("")

def start_server():
    consumer = create_consumer()

    print("Python Kafka Consumer Server started!")
    print(f"Listening to topic \"{TOPIC}\" messages on {BOOTSTRAP_SERVER}...\n")

    for message in consumer:
        print(f"New message: {message.value}")

if __name__=='__main__':
    start_server()
