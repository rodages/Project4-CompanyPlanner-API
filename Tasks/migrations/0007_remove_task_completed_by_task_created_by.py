# Generated by Django 4.0.4 on 2022-05-07 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tasks', '0006_task_assigned_to_checklist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed_by',
        ),
        migrations.AddField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]