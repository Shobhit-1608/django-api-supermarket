from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)

    