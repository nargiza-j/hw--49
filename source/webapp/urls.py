from django.urls import path

from webapp.views import IndexView, TaskView, TaskDeleteView, TaskCreateView, TaskUpdateView, ProjectList, ProjectView, \
    ProjectCreate

urlpatterns = [
    path('', ProjectList.as_view(), name="project_list"),
    path('project/<int:pk>/', ProjectView.as_view(), name="project_view"),
    path('project/add/', ProjectCreate.as_view(), name="project_add"),
    path('tasks', IndexView.as_view(), name="index"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    path('project/<int:pk>/tasks/add/', TaskCreateView.as_view(), name="project_task_add"),
    path('project/<int:pk>/task/delete/', TaskDeleteView.as_view(), name="task_delete"),
    path('project/<int:pk>/task/update/', TaskUpdateView.as_view(), name="task_update")
]
