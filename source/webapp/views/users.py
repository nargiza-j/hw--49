from django.contrib.auth import get_user_model

from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import UsersChooseForm


class UsersChooseView(CreateView):
    model = get_user_model()
    template_name = 'users/choose_user.html'
    form_class = UsersChooseForm
    context_object_name = "user_obj"

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})

