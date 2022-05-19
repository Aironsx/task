from rest_framework import serializers

from tasks.models import Task, Category


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True)
    category = serializers.SlugRelatedField()

    class Meta:
        model = Task
        fields = [
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
        ]

    def validate_author(self, author):
        if not self.context['request'].user == author:
            raise serializers.ValidationError("It's not allowed to change "
                                              "not your task ")
        return author
