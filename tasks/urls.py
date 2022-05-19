from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='task_list'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/done/', views.task_done, name='task_done'),
    path('create-category', views.create_category, name='create_category'),
    path('category/<slug:slug>/', views.category_task, name='category'),
    path('tasks/filter/', views.filter_tasks, name='filter')
    ]
