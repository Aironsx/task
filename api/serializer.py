from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from tasks.models import Category, Task


class CreatableSlugRelatedField(serializers.SlugRelatedField):

    def to_internal_value(self, data):
        try:
            return (
                self.get_queryset().get_or_create(**{self.slug_field: data})[0]
            )
        except ObjectDoesNotExist:
            pass


class CategorySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'author',
            'name',
            'slug'
        )
        read_only_fields = ('slug',)


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    class Meta:
        model = Task
        fields = (
            'id',
            'author',
            'category',
            'is_done',
            'topic',
            'description',
            'created',
            'due_date',
            'coming_soon_task',
            'delayed_task',
        )
        read_only_fields = (
            'created',
            'is_done',
            'coming_soon_task',
            'delayed_task'
        )

    def validate_author(self, author):
        if not self.context['request'].user == author:
            raise serializers.ValidationError("It's not allowed to change "
                                              "not your task ")
        return author
