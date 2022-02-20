from django.contrib.auth import get_user_model

from django.urls import reverse
from django.views.generic import CreateView, ListView

from webapp.forms import UsersChooseForm

User = get_user_model()
class UsersChooseView(CreateView):
    model = User
    template_name = 'users/choose_user.html'
    form_class = UsersChooseForm
    context_object_name = "user_obj"

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class UsersListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = "users_obj"
