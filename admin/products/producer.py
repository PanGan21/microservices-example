import pika

cred = pika.PlainCredentials('guest', 'guest')
params = pika.ConnectionParameters('rabbitmq', 5672, '/', cred)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
