import pika

user_rabbitmq = 'user'
password_rabbitmq = '4RB40nFBB0KOVRsC'

# Conection with the RabbitMQ
credentials = pika.PlainCredentials(user_rabbitmq, password_rabbitmq)
connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials))
channel = connection.channel()

# Queue statement
channel.queue_declare(queue="opa", durable=True, exclusive=False, auto_delete=False)

# Send the message
channel.basic_publish(exchange='opa', routing_key='hello', body='hello!')
print("Message sent!")

# Close the connection
connection.close()