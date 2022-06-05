from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        '<str:username>/tasks/filter/',
        login_required(views.TaskFilterView.as_view()),
        name='filter'
    ),
    path(
        '<str:username>/category/delete/<slug:slug>',
        login_required(views.CategoryDeleteView.as_view()),
        name='delete_category'
    ),
    path(
        '<str:username>/category/all',
        login_required(views.CategoriesListView.as_view()),
        name='all_categories'
    ),
    path(
        '<str:username>/tasks/',
        login_required(views.TasksListView.as_view()),
        name='task_list'
    ),
    path(
        '<str:username>/tasks/<slug:slug>/',
        login_required(views.TaskDetailView.as_view()),
        name='task'
    ),
    path(
        'task/create/',
        login_required(views.CreatTaskView.as_view()),
        name='create_task'
    ),
    path(
        'task/<slug:slug>/edit/',
        login_required(views.TaskUpdateView.as_view()),
        name='edit_task'
    ),
    path(
        'task/<slug:slug>/delete/',
        login_required(views.TaskDeleteView.as_view()),
        name='delete_task'
    ),
    path(
        'task/<slug:slug>/done/',
        views.TaskDoneView.as_view(),
        name='task_done'
    ),
    path(
        'category/create',
        login_required(views.CreatCategoryView.as_view()),
        name='create_category'
    ),
    path(
        '<str:username>/category/<slug:slug>/',
        login_required(views.CategoryDetailView.as_view()),
        name='category'
    ),
]
