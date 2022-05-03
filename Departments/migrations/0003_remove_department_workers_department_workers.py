# Generated by Django 4.0.4 on 2022-05-03 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Workers', '0004_alter_worker_userid'),
        ('Departments', '0002_department_workers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='workers',
        ),
        migrations.AddField(
            model_name='department',
            name='workers',
            field=models.ManyToManyField(default=None, null=True, related_name='departments', to='Workers.worker'),
        ),
    ]
