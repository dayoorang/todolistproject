from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from todo.filters import SnippetFilter
from todo.forms import TodoForm
from todo.models import TodoList


# def todo_create(request):
#     form = TodoForm()
#     print(request.POST)
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         form.save()
#         return redirect('todoapp:list')
#
#     context= {'form': form}
#     return render(request, 'todo/create.html', context)

class TodoCreationView(CreateView):
    model = TodoList
    form_class = TodoForm
    success_url = reverse_lazy('todoapp:list')
    template_name = 'todo/create.html'

class TodoUpdateView(UpdateView):
    model = TodoList
    form_class = TodoForm
    context_object_name = 'target_todo'
    success_url = reverse_lazy('todoapp:list')
    template_name = 'todo/update.html'

class TodoListView(ListView):
    model = TodoList
    context_object_name = 'todo_list'
    template_name = 'todo/list.html'

    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = SnippetFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = SnippetFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context

# class TodoDeleteView(DeleteView):
#     model = TodoList
#     template_name
# def todo_detail(request, pk):
#     form = TodolistForm()
#     tododetail = TodoList.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = TodolistForm(request.POST or None, instance=tododetail)
#         if form.is_valid():
#             form.save()

        # print(request.POST.get('name'))

        # tododetail.is_done = True
        # tododetail.save()
    #
    #     return redirect('todolist')
    # return render(request, 'todo/detail.html', {'tododetail':tododetail, 'form':form})