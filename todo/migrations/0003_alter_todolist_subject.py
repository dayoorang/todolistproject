# Generated by Django 3.2.6 on 2021-08-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210811_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='subject',
            field=models.CharField(blank=True, choices=[('web', 'Web'), ('big_data', 'Big data'), ('nlp', 'NLP'), ('deep_learning', 'Deep learning'), ('machine_learning', 'Machine learning')], max_length=100, null=True),
        ),
    ]