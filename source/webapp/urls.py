from django.urls import path

from webapp.views import IndexView, TaskView, TaskDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    # path('task/add/', TaskCreateView.as_view(), name="task_add"),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name="task_delete")
]