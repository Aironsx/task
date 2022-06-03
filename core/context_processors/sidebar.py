from django.shortcuts import get_object_or_404

from tasks.models import Task, Category


def category(request):
    return {"categories": Category.objects.all()}
