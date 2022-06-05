from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase

from ..models import Category, Task

User = get_user_model()


class TaskCategoryModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test_user')
        cls.category = Category.objects.create(
            author=cls.user,
            name='test_category',
            slug='test_slug'
        )
        cls.task = Task.objects.create(
            author=cls.user,
            topic='test_topic'
        )

    def test_models_have_correct_str_method(self):
        str_value_model_task = self.task.__str__()
        str_value_expect = self.task.topic
        self.assertEqual(str_value_model_task, str_value_expect)

        str_value_model_category = self.category.__str__()
        str_value_expect = self.category.name
        self.assertEqual(str_value_model_category, str_value_expect)

    def test_models_constraint(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(author=self.user, topic='test_topic')
