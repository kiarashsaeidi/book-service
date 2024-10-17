import pika
import json

def send_message_to_queue(book_id):
    # RabbitMQ connection settings
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue for the messages
    channel.queue_declare(queue='book_update_queue', durable=True)

    # Publish the message containing the book_id
    message = json.dumps({'book_id': book_id})
    channel.basic_publish(exchange='', routing_key='book_update_queue', body=message)

    # Close the connection
    connection.close()

send_message_to_queue(59164)