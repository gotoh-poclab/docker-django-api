
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TodoViewSet

routers = routers.DefaultRouter()
routers.register('todo', TodoViewSet)

urlpatterns = [
    path('',include(routers.urls))
]