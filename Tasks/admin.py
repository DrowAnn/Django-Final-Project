from django.contrib import admin
from .models import Task

# Register your models here.


class taskAdmin(admin.ModelAdmin):
    readonly_fields = ("createdDate",)


admin.site.register(Task, taskAdmin)
