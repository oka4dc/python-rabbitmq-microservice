import pika
import time

def send_message():
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    for i in range(10):
        message = f"Hello World! {i}"
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        print(f" [x] Sent '{message}'")
        time.sleep(1)

    connection.close()

if __name__ == "__main__":
    send_message()
"""
  producer:
    build: .
    command: python producer.py
    depends_on:
      - rabbitmq

  consumer:
    build: .
    command: python consumer.py
    depends_on:
      - rabbitmq
"""