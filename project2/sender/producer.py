import pika
import sys
import os
import time
from sender.send import name_prompt

# Add the 'sender' directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def send_message():
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='name_input')

    #message
    #name = name_prompt(name)
    name = input("Enter your name: ")
    # Send the message to the queue
    channel.basic_publish(exchange='',
                          routing_key='name_input',
                          body=name)
    #print(f" [x] Sent '{name}' to the queue")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    send_message()
