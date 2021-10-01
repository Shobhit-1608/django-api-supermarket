from rest_framework.serializers import ModelSerializer
from .models import Queue

class QueueSerializer(ModelSerializer):
    class Meta:
        model = Queue
        fields = '__all__'