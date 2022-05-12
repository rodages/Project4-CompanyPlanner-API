# Generated by Django 4.0.4 on 2022-05-12 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Departments', '0001_initial'),
        ('Checklists', '0003_remove_checklist_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_checklists', to='Departments.department'),
        ),
    ]
