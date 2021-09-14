from django.contrib import admin
from core import models

# Register your models here.

# 書かなくても表示されるが、カスタマイズする時には、このように行う。
class TodoAdmin(admin.ModelAdmin):
    list_display = ("text", "registrationTimeAt")

# 一行登録すると、adminでCRUD操作が行えるようになる。
# class TodoAdminを書かない場合には、後ろのTodoAdminは必要ない。
admin.site.register(models.TodoModel, TodoAdmin)