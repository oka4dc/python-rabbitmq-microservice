import pika
import time

def send_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
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
