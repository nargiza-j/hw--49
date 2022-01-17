from django import forms
from django.forms import widgets

from webapp.models import Task, Type


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Тип", widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = "__all__"

