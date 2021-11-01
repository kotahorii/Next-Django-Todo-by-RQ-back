from django.contrib import admin
from .models import User, Tags, Task

admin.site.register(User)
admin.site.register(Tags)
admin.site.register(Task)
