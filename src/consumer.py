import pika
import json
import os
from dotenv import load_dotenv
import runner

load_dotenv()
RABBITMQ_URI = os.getenv('RABBITMQ_URI')
ANSIBLE_QUEUE = os.getenv('ANSIBLE_QUEUE')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_URI))
channel = connection.channel()
channel.queue_declare(queue=ANSIBLE_QUEUE)


def ansible_runner_event_handler(data):
    print("ansible_runner_event_handler")
    print(data)
    print("=============================")


def ansible_runner_callback(data):
    print("ansible_runner_callback")
    print(data)
    print("+++++++++++++++++++++++++++++")


def callback(channel, method, properties, body):
    print("[x] Received: %r" % body)
    print("[x] Type of body: %r" % type(json.loads(body)))
    runner.run(ansible_runner_event_handler, ansible_runner_callback)


channel.basic_consume(
    queue='ansible', on_message_callback=callback, auto_ack=True)
