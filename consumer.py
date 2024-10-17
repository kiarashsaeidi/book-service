import pika
import json


from api.tasks import invalidate_book_cache

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='book_update_queue', durable=True)

    def callback(ch, method, properties, body):
        data = json.loads(body)
        book_id = data.get('book_id')

        invalidate_book_cache.delay(book_id)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='book_update_queue', on_message_callback=callback)
    print("Starting RabbitMQ consumer...")
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()