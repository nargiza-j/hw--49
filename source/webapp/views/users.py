from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import UsersChooseForm


class UsersChooseView(CreateView):
    model = User
    template_name = 'users/choose_user.html'
    form_class = UsersChooseForm

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

