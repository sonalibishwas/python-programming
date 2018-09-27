import pika
#create connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#create channel
channel = connection.channel()
#declare exchange
channel.exchange_declare(exchange='logs',exchange_type='fanout')
#declare queue
channel.queue_declare(queue='hello',exclusive=True)
#bind the queue
channel.queue_bind(exchange='logs',queue='hello')
#callback
def callback(ch,method,properties,body):
	print ("Received:%r"%body)
#consume message
channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()
