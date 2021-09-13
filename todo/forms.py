from django import forms
from todo.models import TodoList


class TodoForm(forms.ModelForm):
    # is_done = forms.BooleanField(label ='Done')

    class Meta:
        model = TodoList
        fields = ['subject', 'content']

    def __init__(self, *args, **kwargs):
        super(TodoForm,self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['subject'].label = 'subject'
        self.fields['content'].label = 'content'

