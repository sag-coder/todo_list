# from django.contrib.auth.forms import AuthenticationForm
# from django.db.models.base import Model
# from django.forms.forms import Form
# from django.http import request
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
#this loinRequiredMixin is use for restric user for with out loge in
#this mixing need to be over write in setting.py
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.
# def base(request):
#     return HttpResponse('hello')
class LogIn(LoginView):
    model= Task
    template_name = 'login.html'
    # context_object_name = 'tk' this is not working on login
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        
        return reverse_lazy('all-task')


class TaskViews(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'all_tasks'
    template_name = 'all-tasks.html'

    def get_context_data(self, **kwargs):           #this is the method for hiding detail from different user
        context = super().get_context_data(**kwargs)
        # context["color"] ='red'    <this is for demo perpous>
        context['all_tasks'] = context['all_tasks'].filter(user=self.request.user) #user is model object
        context['count'] = context['all_tasks'].filter(complete=False).count() #user is model object complete

        return context
            
        
    
    

class TaskDescription(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    context_object_name = 'form'
    template_name = 'task-create.html'
    # fields = '__all__'
    fields = ['title','description']
    success_url = reverse_lazy('all-task')
    def form_valid(self, form):           #for restrict  user 
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    context_object_name = 'form'
    template_name = 'task-create.html'
    # fields = '__all__'
    fields = ['title','description','complete']
    success_url = reverse_lazy('all-task')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'confirmation.html'
    success_url = reverse_lazy('all-task') 