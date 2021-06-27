from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

# Create your views here.
# def base(request):
#     return HttpResponse('hello')

class TaskViews(ListView):
    model = Task
    context_object_name = 'all_tasks'
    template_name = 'all-tasks.html'

class TaskDescription(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'

class TaskCreate(CreateView):
    model = Task
    context_object_name = 'form'
    template_name = 'task-create.html'
    fields = '__all__'
    success_url = reverse_lazy('all-task')

class TaskUpdate(UpdateView):
    model = Task
    context_object_name = 'form'
    template_name = 'task-create.html'
    fields = '__all__'
    success_url = reverse_lazy('all-task')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'confirmation.html'
    success_url = reverse_lazy('all-task') 