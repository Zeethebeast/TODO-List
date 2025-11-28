from django.urls import path
from .views import (
    TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView,
    toggle_complete, TodoDetailView
)

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
    path('todo/add/', TodoCreateView.as_view(), name='todo_add'),
    path('todo/<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_edit'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/toggle/', toggle_complete, name='todo_toggle'),
]
