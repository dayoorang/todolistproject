from django.urls import path, include

from todo.views import TodoListView,TodoUpdateView, todo_create_view

app_name = 'todoapp'

urlpatterns = [
    path('', TodoListView.as_view(), name='list' ),
    path('create/<int:pk>', todo_create_view, name='create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update')
    # path('create/', todo_create, name='create'),

    # path('<int:pk>/', todo_detail, name='detail')

]