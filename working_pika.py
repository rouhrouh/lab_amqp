import pika
import ssl
from decouple import config


ssl_context = ssl.create_default_context()
parameters = pika.URLParameters(config('AMQPS_URL'))
parameters.ssl_options = pika.SSLOptions(context=ssl_context)


connection = pika.BlockingConnection(parameters)
channel = connection.channel()


def on_message_received(ch, method, properties, body):
    print("###################")
    print(f"{body.decode()}")
    print("###################")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue=config('QUEUE_NAME'),
    on_message_callback=on_message_received,
    auto_ack=False
)

channel.start_consuming()
