from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectList(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = 'projects'
    paginate_by = 3


class ProjectView(DetailView):
    model = Project
    template_name = 'projects/project_view.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.object.tasks.all()
        context['tasks'] = tasks
        return context


class ProjectCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'webapp.add_project'
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'

    def form_valid(self, form):
        response = super(ProjectCreate, self).form_valid(form)
        self.object.users.add(self.request.user)
        return response


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_project'
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "webapp.delete_project"
    model = Project
    template_name = "projects/project_delete.html"
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project_list')
