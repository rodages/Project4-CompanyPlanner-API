# Generated by Django 4.0.4 on 2022-05-07 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tasks', '0010_task_section_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edited_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='extra_from_checklist_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]