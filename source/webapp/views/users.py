from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse
from django.views.generic import ListView, UpdateView

from webapp.forms import ProjectUsersForm
from webapp.models import Project

User = get_user_model()


class ChangeUsersInProjectView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'users/change_users.html'
    form_class = ProjectUsersForm
    permission_required = "webapp.change_user_in_own_project"

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()


class UsersListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = "users_obj"
    permission_required = "accounts.can_look_list_of_users"
