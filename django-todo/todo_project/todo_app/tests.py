from django.test import TestCase
from django.urls import reverse
from .models import Todo
import datetime

class TodoModelTests(TestCase):
    def test_create_todo(self):
        t = Todo.objects.create(title="Test", description="desc", due_date=datetime.date.today())
        self.assertEqual(Todo.objects.count(), 1)
        self.assertFalse(t.is_completed)

class TodoViewTests(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title="My todo", description="ok", due_date=datetime.date.today())

    def test_home_view_lists_todos(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My todo")

    def test_create_todo_via_form(self):
        resp = self.client.post(reverse('todo_add'), {
            'title': 'Posted',
            'description': 'from test',
            'due_date': datetime.date.today().isoformat(),
            'is_completed': False,
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Todo.objects.filter(title='Posted').exists())

    def test_edit_todo(self):
        resp = self.client.post(reverse('todo_edit', args=[self.todo.pk]), {
            'title': 'Updated',
            'description': 'changed',
            'due_date': self.todo.due_date.isoformat(),
            'is_completed': False,
        }, follow=True)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated')

    def test_delete_todo(self):
        resp = self.client.post(reverse('todo_delete', args=[self.todo.pk]), follow=True)
        self.assertEqual(Todo.objects.count(), 0)

    def test_toggle_complete(self):
        self.assertFalse(self.todo.is_completed)
        resp = self.client.get(reverse('todo_toggle', args=[self.todo.pk]), follow=True)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_completed)
