from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectList(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = 'projects'


class ProjectView(DetailView):
    model = Project
    template_name = 'projects/project_view.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.object.tasks.all()
        context['tasks'] = tasks
        return context


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'
