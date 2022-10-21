from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(ZoneCat)
admin.site.register(Article)


class AdminComment(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'website', 'msg')


admin.site.register(Comment, AdminComment)