from django import forms
from django.forms import widgets

from webapp.models import Task, Type, Project


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Тип", widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = "__all__"


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label='Поиск')


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = "__all__"
