from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

# Create your views here.
# def base(request):
#     return HttpResponse('hello')

class TaskViews(ListView):
    model = Task
    context_object_name = 'all_tasks'
    template_name = 'all-tasks.html'
