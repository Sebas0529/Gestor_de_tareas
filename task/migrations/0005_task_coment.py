# Generated by Django 4.2 on 2023-04-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_remove_task_coments'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='coment',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]
