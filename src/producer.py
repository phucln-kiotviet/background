# import pika
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv()
# RABBITMQ_URI = os.getenv('RABBITMQ_URI')
# ANSIBLE_QUEUE = os.getenv('ANSIBLE_QUEUE')


# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host=RABBITMQ_URI))
# channel = connection.channel()

# channel.queue_declare(queue=ANSIBLE_QUEUE)
# channel.basic_publish(exchange='', routing_key=ANSIBLE_QUEUE,
#                       body=json.dumps({"name": "phuc"}))
# print("[x] Sent ")
# connection.close()
