import django_filters
from django import forms

from todo.models import TodoList


class SnippetFilter(django_filters.FilterSet):
    SUBJECT_CHOICES = (
        ('Web', 'Web'),
        ('Big data', 'Big data'),
        ('NLP', 'NLP'),
        ('Deep learning', 'Deep learning'),
        ('Machine learning', 'Machine learning')
    )
    subject = django_filters.ChoiceFilter(label='',choices=SUBJECT_CHOICES,
                                widget=forms.Select(attrs={'class':'form-control me-2'}))
    class Meta:
        model = TodoList
        fields = ['subject']

