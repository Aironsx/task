from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Category, Task

User = get_user_model()


class TaskCreateFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='test_user')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

    def setUp(self) -> None:
        self.category = Category.objects.create(
            author=self.user,
            name='test_name',
            slug='test_slug'
        )

    def test_create_new_task_authorized_client(self):
        task_before_creation = Task.objects.count()
        form_data = {
            'topic': 'topic_test'
        }
        response = self.authorized_client.post(
            reverse('tasks:create_task'),
            data=form_data,
            follow=True,
        )
        self.assertEqual(Task.objects.count(), task_before_creation + 1)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_new_task_guest_client(self):
        task_before_creation = Task.objects.count()
        form_data = {
            'topic': 'topic_test'
        }
        response = self.guest_client.post(
            reverse('tasks:create_task'),
            data=form_data,
            follow=True,
        )
        self.assertEqual(Task.objects.count(), task_before_creation)
        self.assertRedirects(response, '/auth/login/?next=/task/create/')

    def test_edit_task(self):
        task = Task.objects.create(
            topic='topic_test',
            author=self.user,
            category=self.category
        )
        task_before_editing = Task.objects.count()
        form_data = {
            'topic': 'edited text',
            'category': 1
        }
        response = self.authorized_client.post(
            reverse('tasks:edit_task', args=[task.slug]),
            data=form_data,
            follow=True
        )
        self.assertEqual(Task.objects.count(), task_before_editing)

        edited_task = Task.objects.get(pk=1)
        self.assertEqual(edited_task.topic, 'edited text')
        self.assertEqual(edited_task.author, self.user)
        self.assertEqual(edited_task.category.name, self.category.name)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class CategoryCreateFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='test_user')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

    def test_create_new_category_authorized_client(self):
        category_before_creation = Task.objects.count()
        form_data = {
            'name': 'name_test'
        }
        response = self.authorized_client.post(
            reverse('tasks:create_category'),
            data=form_data,
            follow=True,
        )
        self.assertEqual(
            Category.objects.count(),
            category_before_creation + 1
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_create_new_category_guest_client(self):
        category_before_creation = Task.objects.count()
        form_data = {
            'name': 'name_test'
        }
        response = self.guest_client.post(
            reverse('tasks:create_category'),
            data=form_data,
            follow=True,
        )
        self.assertEqual(Category.objects.count(), category_before_creation)
        self.assertRedirects(response, '/auth/login/?next=/category/create')
