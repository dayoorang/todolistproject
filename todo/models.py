from django.db import models
from datetime import datetime
# Create your models here.
from projectapp.models import Project
from django.contrib.humanize.templatetags import humanize


SUBJECT_CHOICES = (
            ('Web', 'Web' ),
            ('Big data', 'Big data' ),
            ('NLP', 'NLP' ),
            ('Deep learning', 'Deep learning' ),
            ('Machine learning', 'Machine learning')
)

class TodoList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='todolist', null=True)
    subject = models.CharField(max_length=100, blank=True, null=True, choices = SUBJECT_CHOICES)
    content = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def get_date(self):
    #     time = datetime.now()
    #     if self.created_at.day == time.day:
    #         return str(time.hour - self.created_at.hour) + " hours ago"
    #     else:
    #         if self.created_at.month == time.month:
    #             return str(time.day - self.created_at.day) + " days ago"
    #         else:
    #             if self.created_at.year == time.year:
    #                 return str(time.month - self.created_at.month) + " months ago"
    #     return self.created_at
    # def get_date(self):
    #     return humanize.naturaltime(self.created_at)