from django import forms
from todo.models import TodoList


class TodoForm(forms.ModelForm):
    # is_done = forms.BooleanField(label ='Done')
    class Meta:
        model = TodoList
        fields = ['subject', 'content']