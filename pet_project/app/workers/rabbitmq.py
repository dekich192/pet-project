import pika
import json
import asyncio
from typing import Any, Callable, Dict
from ..config.settings import get_settings

settings = get_settings()

class RabbitMQConsumer:
    def __init__(self, queue_name: str, callback: Callable[[Dict[str, Any]], None]):
        self.queue_name = queue_name
        self.callback = callback
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(settings.rabbitmq_url)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        
        def on_message(ch, method, properties, body):
            try:
                message = json.loads(body)
                self.callback(message)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except json.JSONDecodeError:
                print(f"Error decoding message: {body}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            except Exception as e:
                print(f"Error processing message: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
        
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=on_message
        )

    def start_consuming(self):
        print(f"Starting consumer for queue: {self.queue_name}")
        self.channel.start_consuming()

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

class RabbitMQProducer:
    def __init__(self):
        self.connection = None
        self.channel = None

    def connect(self):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(settings.rabbitmq_url)
        )
        self.channel = self.connection.channel()

    def publish(self, queue_name: str, message: Dict[str, Any]):
        if not self.connection or self.connection.is_closed:
            self.connect()
        
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))

    def close(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
