from django import forms
from todo.models import TodoList


class TodoForm(forms.ModelForm):
    # is_done = forms.BooleanField(label ='Done')
    # SUBJECT_CHOICES = (
    #     ('Web', 'Web'),
    #     ('Big data', 'Big data'),
    #     ('NLP', 'NLP'),
    #     ('Deep learning', 'Deep learning'),
    #     ('Machine learning', 'Machine learning')
    # )
    #
    # subject = forms.ChoiceField(choices = SUBJECT_CHOICES)
    # content = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Content',
    #                                                          'class': 'my-2'}))
    class Meta:
        model = TodoList
        fields = ['subject', 'content']
        # widgets = {'project': forms.HiddenInput()}