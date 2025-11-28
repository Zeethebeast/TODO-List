from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Todo
from .forms import TodoForm

class TodoListView(ListView):
    model = Todo
    template_name = "todo_app/home.html"
    context_object_name = "todos"

class TodoDetailView(DetailView):
    model = Todo
    template_name = "todo_app/detail.html"
    context_object_name = "todo"

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo_app/todo_form.html"
    success_url = reverse_lazy('home')

class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo_app/todo_form.html"
    success_url = reverse_lazy('home')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo_app/todo_confirm_delete.html"
    success_url = reverse_lazy('home')

# small view to toggle completion
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('home')
