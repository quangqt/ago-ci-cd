import os
from dataclasses import dataclass
from kafka import KafkaProducer
@dataclass
class ProducerConfig:
    bootstrap_server = "127.0.0.1:9092"
    topic = "security"
class Producer:
    def __init__(self, config: ProducerConfig):
        # self.client = KafkaProducer(bootstrap_servers = config.bootstrap_server,key_serializer=str.encode,value_
        self.client = KafkaProducer(
            bootstrap_servers="pkc-5m9gg.eastasia.azure.confluent.cloud:9092",
            security_protocol="SASL_SSL",
            sasl_mechanism="PLAIN",
            sasl_plain_username=username,
            sasl_plain_password=password
        )
        self.topic = config.topic
    def produce(self, msg: str):
        try:
            future = self.client.send(self.topic, key="key2", value=msg)
            _ = future.get(timeout=10)
            print(f"Successful produced message to topic: {self.topic}")
        except Exception as e:
            print(f"Could not produce to topic: {self.topic}. Error: {e}")
config = ProducerConfig()
redpanda_producer = Producer(config)
redpanda_producer.produce("Hello Security2")