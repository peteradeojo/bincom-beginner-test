from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_task', views.new_task, name='new_task'),
    path('task/<int:task_id>/toggle', views.toggle, name='toggle'),
    path('task/<int:task_id>/delete', views.delete, name='delete')
]
