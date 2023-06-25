import pika
from pika.exchange_type import ExchangeType
# lesson 10a
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# we don't need to declare queue

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout) # exchange name and type

message = 'Hello I want to broadcast this message'
# we route with exchange name and type without routing key
channel.basic_publish(exchange='pubsub', routing_key='', body=message)

print(f'sent message: {message}')

connection.close()