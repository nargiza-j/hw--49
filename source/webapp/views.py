from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.order_by('created_at')
        context['tasks'] = tasks
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        context['task'] = task
        return context

