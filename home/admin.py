from django.contrib import admin
from .models import person, detail, food

admin.site.register(person)
admin.site.register(detail)
admin.site.register(food)