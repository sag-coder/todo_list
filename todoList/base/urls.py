from django.urls import path
from . import views

urlpatterns=[
    path('',views.TaskViews.as_view(), name='all-task'),
    path('task/<int:pk>/',views.TaskDescription.as_view(), name = 'task-description'),
    path('task-create/',views.TaskCreate.as_view(), name = 'task-create'),
    path('taskUpdate/<int:pk>/',views.TaskUpdate.as_view(), name= 'task-update'),
    path('taskDelete/<int:pk>/',views.TaskDelete.as_view(), name= 'task-delete'),
    
]
