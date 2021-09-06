from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#
class Project(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='project')
    topic = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True,null=True)
    image = models.ImageField(upload_to='project/%Y%m%d', blank=True, null=True)

    def __str__(self):
        return f'{self.topic}'

