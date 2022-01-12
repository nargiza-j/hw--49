from django.shortcuts import render

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

