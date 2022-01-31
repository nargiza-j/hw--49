from django.views.generic import ListView, DetailView, CreateView

from webapp.models import Project


class ProjectList(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = 'projects'


class ProjectView(DetailView):
    pass


class ProjectCreate(CreateView):
    pass