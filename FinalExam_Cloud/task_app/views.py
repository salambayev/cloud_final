from django.shortcuts import render
from .models import Task
import pika
from registration.models import User
# Create your views here.

def get_tasks(request):
    if (request.method=='POST'):
        text = request.POST['text']

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='firstq')
        body = request.user.id + "+" + "null" + "+" +  text
        channel.basic_publish(exchange='',
                              routing_key='first_queue',
                              body=body)
        connection.close()
    if (request.user.is_authenticated):
        tasks = Task.objects.filter(user = request.user)
        return render(request, 'index.html', {'tasks':tasks })
    else:
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks':tasks })


