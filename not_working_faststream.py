from faststream import FastStream
from faststream.rabbit import RabbitBroker
from faststream.security import BaseSecurity
from decouple import config

import ssl

ssl_context = ssl.create_default_context()
security = BaseSecurity(ssl_context=ssl_context)

broker = RabbitBroker(config('AMQPS_URL'), security=security)
app = FastStream(broker)


@broker.subscriber(config('QUEUE_NAME'))
async def handle_msg(body) -> str:
    print('body')
