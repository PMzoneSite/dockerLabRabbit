import pika
import time

url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

connection = pika.BlockingConnection(url_params)

channel = connection.channel()

exchange_name = 'headers_logs'
exchange_type = 'headers'

channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

queue_name = 'my_queue'

channel.queue_declare(queue=queue_name)

routing_key = ' '
headers
    binding_arguments = {
    'x-match':'any'
    'header1':'value1'
} 

channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key, arguments = binding_arguments) )

counter = 1
try:
    while True:
        message = f'Hello, RabbitMQ - Message #{counter}'
        headers = {
            'header1':'value1'
        }
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message, properties = pika.BasicProperties(headers=headers)))
        print(f"Sent: '{message}' with routing key '{routing_key}'")
        counter += 1
        time.sleep(1)  
except KeyboardInterrupt:
    print("\nWaiting...")
finally:
    channel.close()
    connection.close()
