# Generated by Django 3.2.6 on 2021-08-30 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_auto_20210830_2121'),
        ('todo', '0009_alter_todolist_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='todolist', to='projectapp.project'),
        ),
    ]
