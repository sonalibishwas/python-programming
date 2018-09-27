import pika
#create a TCP connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# create a channel over connection to publish data 
channel = connection.channel()
#declare an exchange on which message needs to be published
channel.exchange_declare(exchange='logs',exchange_type='fanout')
message = "Hello World"
channel.basic_publish(exchange='logs',routing_key='',body=message)
print "Sent:Hello World"
connection.close()
