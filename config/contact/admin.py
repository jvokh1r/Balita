from django.contrib import admin
from .models import *


class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_solved')


admin.site.register(Contact, AdminContact)


