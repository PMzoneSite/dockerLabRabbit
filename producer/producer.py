import pika
import time

url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

connection = pika.BlockingConnection(url_params)

channel = connection.channel()

exchange_name = 'direct_logs'
exchange_type = 'direct'

channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

queue_name = 'my_queue'

channel.queue_declare(queue=queue_name)

routing_key = 'info'
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

counter = 1
try:
    while True:
        message = f'Hello, RabbitMQ - Message #{counter}'
        channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)
        print(f"Sent: '{message}' with routing key '{routing_key}'")
        counter += 1
        time.sleep(1)  # Ïàóçà 1 ñåêóíäà ìåæäó ñîîáùåíèÿìè
except KeyboardInterrupt:
    print("\nÎñòàíîâêà îòïðàâêè ñîîáùåíèé...")
finally:
    channel.close()
    connection.close()
