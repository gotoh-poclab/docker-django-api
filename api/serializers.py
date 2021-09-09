from rest_framework import serializers
from core.models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('id', 'text')
