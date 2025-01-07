from django.urls import path
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView, TaskStatusChangeView, TaskUpdateView)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task-detail"),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/edit/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/status/<int:pk>/', TaskStatusChangeView.as_view(), name='task-status'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
