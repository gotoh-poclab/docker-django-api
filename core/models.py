from django.db import models

# Create your models here.

# シンプルなTodoを作成
class TodoModel(models.Model):
    text = models.TextField()
    registrationTimeAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)