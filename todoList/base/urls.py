from django.urls import path
from . import views

urlpatterns=[
    path('',views.TaskViews.as_view(),name='all-task'),
]
