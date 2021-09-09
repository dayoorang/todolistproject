from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from todo.forms import TodoForm
from todo.models import TodoList


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    success_url = reverse_lazy('projectapp:list')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 3


class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = 'target_projcet'
    success_url = reverse_lazy('projectapp:list')
    template_name = 'projectapp/delete.html'

class ProjectDetailView(DetailView,FormMixin):
    model = Project
    context_object_name = 'target_project'
    form_class = TodoForm
    template_name = 'projectapp/detail.html'

    def form_valid(self, form):
        form.instance.project = self.object
        return super().form_valid(form)

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    context_object_name = 'target_project'
    template_name = 'projectapp/update.html'

    #
    # def get_context_data(self, **kwargs):
    #     todo_list = TodoList.objects.filter(project=self.object)
    #     print('todo_list', todo_list)
    #     return super().get_context_data(object_list=todo_list,**kwargs)