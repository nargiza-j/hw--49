from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm, SearchForm
from webapp.models import Task, Project


class IndexView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class TaskView(TemplateView):
    template_name = 'tasks/task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        context['task'] = task
        return context


class TaskCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_task_in_own_project'
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        return super().has_permission() and self.request.user in project.users.all()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={"pk": self.object.project.pk})


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "webapp.change_task_in_own_project"
    model = Task
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={"pk": self.object.project.pk})

    def has_permission(self):
        return super().has_permission() and self.get_object().project.users.filter(pk=self.request.user.pk).exists()


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    context_object_name = 'task'
    success_url = reverse_lazy('webapp:project_list')
    permission_required = "webapp.delete_task_in_own_project"

    def has_permission(self):
        return super().has_permission() and self.get_object().project.users.filter(pk=self.request.user.pk).exists()


# class TaskUpdateView(View):
#     def get(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs.get("pk"))
#         form = TaskForm(initial={
#             "summary": task.summary,
#             "description": task.description,
#             "status": task.status,
#             "type": task.type.all()
#         })
#         return render(request, 'tasks/task_update.html', {'task': task, "form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = TaskForm(data=request.POST)
#         task = get_object_or_404(Task, pk=kwargs['pk'])
#         if form.is_valid():
#             type = form.cleaned_data.pop('type')
#             task.type.set(type)
#             task.summary = form.cleaned_data.get('summary')
#             task.description = form.cleaned_data.get('description')
#             task.status = form.cleaned_data.get('status')
#             task.save()
#             return redirect('index')
#         return render(request, 'tasks/task_update.html', {"task": task, "form": form})


# class TaskDeleteView(View):
#     def get(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs.get('pk'))
#         return render(request, "tasks/task_delete.html", {"task": task})
#
#     def post(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs['pk'])
#         task.delete()
#         return redirect("index")
