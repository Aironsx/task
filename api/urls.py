from django.urls import include, path
from rest_framework import routers

from .views import TasksViewSet, CategoryViewSet

v1_router = routers.DefaultRouter()
v1_tasks = v1_router.register('tasks', TasksViewSet, basename='tasks')
v1_category = v1_router.register(
    'category',
    CategoryViewSet,
    basename='category'
)

app_name = 'api'

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
