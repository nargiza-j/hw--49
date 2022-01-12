from django.contrib import admin

from webapp.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'type']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'type', 'status']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type)
