from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('task/<str:username>/', views.TestView.as_view(), name='test'),
    path(
        'tasks/<str:username>/',
        login_required(views.TasksListView.as_view()),
        name='task_list'
    ),
    path(
        'tasks/<str:username>/<int:task_id>/',
        login_required(views.TaskDetailView.as_view()),
        name='task'
    ),
    path(
        'task/create/',
        login_required(views.CreatTaskView.as_view()),
        name='create_task'
    ),
    path(
        'task/<int:task_id>/edit/',
        views.TaskUpdateView.as_view(),
        name='edit_task'
    ),
    path(
        'task/<int:task_id>/done/',
        views.TaskDoneView.as_view(),
        name='task_done'
    ),
    path(
        'create-category',
        login_required(views.CreatCategoryView.as_view()),
        name='create_category'
    ),
    path(
        'category/<slug:slug>/',
        login_required(views.CategoryDetailView.as_view()),
        name='category'
    ),
    path(
        'tasks/filter/',
        login_required(views.TaskFilterView.as_view()),
        name='filter'
    )
]
