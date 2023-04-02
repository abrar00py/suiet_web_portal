from django.contrib import admin
from .models import NoticeBoard_Engineering, Events, Engineering_Faculty
# Register your models here.
class Faculty_custom(admin.ModelAdmin):
    list_display =['name','Teaching_Experience','qualification']

admin.site.register(NoticeBoard_Engineering)
admin.site.register(Events)
admin.site.register(Engineering_Faculty,Faculty_custom)