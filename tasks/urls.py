from django.urls import path
from . import views

urlpatterns = [
    path('createtask/', views.create_task, name='create_task'),
    path('showtask/', views.show_task, name='show_task'),
    path('edittask/<int:id>/', views.edit_task, name='edit_task')
]