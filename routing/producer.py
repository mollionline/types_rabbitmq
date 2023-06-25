import pika
from pika.exchange_type import ExchangeType
# lesson 12a
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)
# channel.exchange_declare(exchange='directroutingechange', exchange_type=ExchangeType.direct)

# message should to send to all kinds of microservices

user_paymetns_message = 'A european user paid for something'

channel.basic_publish(exchange='mytopicexchange', routing_key='user.europe.payments', body=user_paymetns_message)
# channel.basic_publish(exchange='directroutingechange', routing_key='paymentsonly', body=user_paymetns_message)

print(f'sent message: {user_paymetns_message}')

# message should send to only analytics microservice

business_order_message = 'A european business ordered goods'

channel.basic_publish(exchange='mytopicexchange', routing_key='business.europe.order', body=business_order_message)
# channel.basic_publish(exchange='directroutingechange', routing_key='both', body=business_order_message)

print(f'sent message: {business_order_message}')

connection.close()