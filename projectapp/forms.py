from django.forms import ModelForm

from projectapp.models import Project
from django import forms

class ProjectCreationForm(ModelForm):
    # topic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject',
    #                                                          'class': 'my-2'}))
    # image = forms.FileField(widget=forms.ClearableFileInput(attrs={'placeholder': '비밀번호 입력',
    #                                                               'class': 'my-2' }))
    # description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'description',
    #
    #                                                               'class': 'my-2' }))
    class Meta:
        model = Project
        fields = ['topic','image','description']
        widgets = {
            'image' : forms.ClearableFileInput()
        }
    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


        self.fields['image'].required = False

        self.fields['topic'].label = 'Subject'
        self.fields['image'].label = 'image'
        self.fields['description'].label = 'description'

