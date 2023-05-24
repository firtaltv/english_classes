from django.contrib import admin

from classes.models import EnglishClass
from users.models import User

# Register your models here.

admin.site.register(User)
admin.site.register(EnglishClass)