from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('edit/<str:pk>/', views.edit_Task, name='edit'),
    path('delete/<str:pk>/', views.delete_Task, name='delete'),
]