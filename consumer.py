import pika

user_rabbitmq = 'user'
password_rabbitmq = '123'

# Conection with the RabbitMQ
credentials = pika.PlainCredentials(user_rabbitmq, password_rabbitmq)
connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials))
channel = connection.channel()

# Queue statement
channel.queue_declare(queue='opa', durable=True)

# Callback function to process incoming message
def callback(ch, method, properties, body):
    # Escreve a mensagem no arquivo
    with open('mensagens.txt', 'a') as f:
        f.write(body.decode('utf-8') + '\n')

# Subscribing the callback function to the queue
channel.basic_consume(queue='opa', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting mensage. Press CTRL+C to exit.')
channel.start_consuming()