from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.order_by('-created_at')
        context['tasks'] = tasks
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        context['task'] = task
        return context


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, "task_create.html", {'form': form})


# class TaskDeleteView(TemplateView):
#     template_name = 'index.html'
#
#     def get(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs.get('pk'))
#         task.delete()
#         return super().get(request)


class TaskUpdateView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        form = TaskForm(initial={
            "summary": task.summary,
            "description": task.description,
            "status": task.status,
            "type": task.type
        })
        return render(request, 'task_update.html', {'task': task, "form": form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        task = get_object_or_404(Task, pk=kwargs['pk'])
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.type = form.cleaned_data.get('type')
            task.save()
            return redirect('index')
        return render(request, 'task_update.html', {"task": task, "form": form})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, "task_delete.html", {"task": task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect("index")
