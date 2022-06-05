from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from ..models import Task, Category

User = get_user_model()


class StaticPagesURLTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.user = User.objects.create_user(username='test_user')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.user)

        cls.category = Category.objects.create(
            author=cls.user,
            name='test_name',
            slug='test_slug',
        )
        cls.task = Task.objects.create(
            author=cls.user,
            topic='test_topic'
        )

        cls.unexist_page = '/unexist_page/'

        cls.templates_url_pub_names = (
            ('/', 'tasks/index.html'),
        )
        cls.templates_url_not_pub_names = (
            (f'/{cls.user}/tasks/filter/', 'tasks/tasks_list.html'),
            (f'/{cls.user}/category/all', 'tasks/categories_list.html'),
            (f'/{cls.user}/tasks/', 'tasks/tasks_list.html'),
            (f'/{cls.user}/tasks/{cls.task.slug}/', 'tasks/direct_task.html'),
            ('/task/create/', 'tasks/create_task.html'),
            (
                f'/task/{cls.task.slug}/edit/',
                'tasks/create_task.html'
            ),
            (f'/task/{cls.task.slug}/delete/',
             'tasks/confirm_task_delete.html'),
            (f'/category/create', 'tasks/create_category.html'),
            (
                f'/{cls.user}/category/{cls.category.slug}/',
                'tasks/task_by_category.html'
            )
        )

    def test_public_url_for_guest_user(self):
        for response, _ in self.templates_url_pub_names:
            with self.subTest(address=response):
                response = self.guest_client.get(response)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_not_public_url_for_authorized_user(self):
        for response, _ in self.templates_url_not_pub_names:
            with self.subTest(address=response):
                response = self.authorized_client.get(response)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_not_public_url_for_guest_user(self):
        for response, _ in self.templates_url_not_pub_names:
            with self.subTest(address=response):
                response = self.guest_client.get(response)
                self.assertEqual(response.status_code, HTTPStatus.FOUND)


    def test_unexist_url(self):
        response = self.guest_client.get(self.unexist_page)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_urls_use_correct_template_for_pub_page(self):
        for response, template in self.templates_url_pub_names:
            with self.subTest(address=response):
                response = self.guest_client.get(response)
                self.assertTemplateUsed(response, template)

    def test_urls_use_correct_template_for_not_pub_page(self):
        for response, template in self.templates_url_not_pub_names:
            with self.subTest(address=response):
                response = self.authorized_client.get(response)
                self.assertTemplateUsed(response, template)
