import pika
import json

cred = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('rabbitmq', 5672, '/', cred)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body), properties=properties)
