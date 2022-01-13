from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView

from webapp.forms import TaskForm
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


# class TaskCreateView(TemplateView):
#
#     def get_context_data(self, **kwargs):
#         if self.request.method == "GET":
#             form = TaskForm()
#             kwargs['form'] = form
#             context = super().get_context_data(**kwargs)
#             print(kwargs)
#             return context
#         else:
#             form = TaskForm(data=self.request.POST)
#             if form.is_valid():
#                 kwargs['task'] = form.save()
#                 context = super().get_context_data(**kwargs)
#                 return context
#             return render(self.request, "task_create.html", {'form': form})


class TaskDeleteView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return super().get(request)

