from customer.models import Customer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import CustomerSerializer

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

