from pika import ConnectionParameters, BasicProperties

connection_params = ConnectionParameters(
    host="localhost",
    port=5672
)

def main():
    with pika.BlockingConnection(connection_params) as conn:
        channel = conn.channel()
        channel.queue_declare(queue="test_queue")
        
        def callback(ch, method, properties, body):
            print("[x] Received %r" % body)
            
        channel.basic_consume(
            queue="test_queue",
            on_message_callback=callback,
            auto_ack=True
        )
        print("[*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()

if __name__ == "__main__":
    main()
