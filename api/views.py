from django.shortcuts import render
from rest_framework import viewsets, generics
from core.models import TodoModel
from api.serializers import TodoSerializer

# Create your views here.


# ************************
# Todoの全データ
# ************************

class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
       serializer.save(author=self.request.user)
