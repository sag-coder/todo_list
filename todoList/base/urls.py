from django.urls import path
from . import views
#we can access views is urls.py
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('login/',views.LogIn.as_view(), name='logInPage'),
    path('logout/',LogoutView.as_view(next_page='logInPage'), name='logout'),
    path('',views.TaskViews.as_view(), name='all-task'),
    path('task/<int:pk>/',views.TaskDescription.as_view(), name = 'task-description'),
    path('task-create/',views.TaskCreate.as_view(), name = 'task-create'),
    path('taskUpdate/<int:pk>/',views.TaskUpdate.as_view(), name= 'task-update'),
    path('taskDelete/<int:pk>/',views.TaskDelete.as_view(), name= 'task-delete'),
    
]
