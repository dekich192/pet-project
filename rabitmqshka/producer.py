import pika

connection_params = pika.ConnectionParameters(
    host="localhost",
    port=5672
)

def main():
    with pika.BlockingConnection(connection_params) as conn:
        channel = conn.channel()
        channel.queue_declare(queue="test_queue")
        
        channel.basic_publish(
            exchange="",
            routing_key="test_queue",
            body="Hello World!",
        )
        print("[x] Sent 'Hello World!'")

if __name__ == "__main__":
    main()