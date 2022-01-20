from django.contrib import admin

from webapp.models import Task, Status, Type


class TaskInline(admin.TabularInline):
    model = Task.type.through


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status']
    list_filter = ['status', 'type']
    search_fields = ['summary', 'type', 'status']
    fields = ['summary', 'description', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [TaskInline, ]
    exclude = ('type',)


class TypeAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(Status)
admin.site.register(Type, TypeAdmin)
