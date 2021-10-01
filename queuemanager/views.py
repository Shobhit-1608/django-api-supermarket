# from queuemanager.models import Queue
from typing import Generic
from django.shortcuts import render
from rest_framework import generics
from .models import Queue
# from rest_framework.viewsets import ModelViewSet
# from .serializer import  QueueSerializer
# from customer import views
# class QueueViewSet(ModelViewSet):
#     serializer_class = QueueSerializer
#     queryset = Queue.objects.all()

from . import services

def fetch_number(request):
    queue = Queue()
    queue.length_queue = services.get_queuelength()
    if queue.length_queue<=5:
        queue.choice_estimated = "get in line"
    else:
        queue.choice_estimated = "wait for a while"
    return render (request, 'home.html', {'queue':queue.length_queue})

