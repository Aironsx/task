from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author'
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Name',
        unique=True
    )
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Activity types'
        verbose_name_plural = 'Activity type'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='task'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Activity type',
        related_name='task'
    )
    is_regular = models.BooleanField(
        verbose_name='Regular',
        default=False
    )
    is_done = models.BooleanField(
        null=False,
        default=False,
        verbose_name='Task done'
    )
    topic = models.CharField(
        max_length=200,
        verbose_name='Topic'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Full description'
    )
    created = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    coming_soon_task = models.BooleanField(default=False)
    delayed_task = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Task'

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse('tasks:task', kwargs={'task_id': self.pk})
