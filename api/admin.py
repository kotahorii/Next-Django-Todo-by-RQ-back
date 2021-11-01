from django.contrib import admin
from .models import User, Tag, Task

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Task)
