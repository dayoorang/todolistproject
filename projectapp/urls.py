from django.contrib import admin
from django.urls import path, include

from projectapp.views import (ProjectCreateView,
                              ProjectListView,
                              ProjectDeleteView,
                              ProjectDetailView,
                              ProjectUpdateView)

app_name='projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProjectUpdateView.as_view(), name='update'),

    path('list/', ProjectListView.as_view(), name='list'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),

    path('delete/<int:pk>', ProjectDeleteView.as_view(), name='delete')

]