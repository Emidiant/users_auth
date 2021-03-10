from django.contrib import admin
from .models import User

# adding the ability to create a user through administrative tools
admin.site.register(User)
