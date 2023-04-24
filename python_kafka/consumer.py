from kafka import KafkaConsumer
import json

json_value_deserializer = lambda m : json.loads(m.decode('utf-8'))
str_value_deserializer = lambda m : m.decode('utf-8')

consumer = KafkaConsumer('my-topic-name',
                         group_id='my-group-2',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=str_value_deserializer)
                        #  value_deserializer=json_value_deserializer)

for message in consumer:
    print("topic | partition | offset")
    print("--------------------------")
    print(f"{message.topic} | {message.partition} | {message.offset}")
    print(f"key: {message.key}")
    print(f"value: {message.value}\n")
