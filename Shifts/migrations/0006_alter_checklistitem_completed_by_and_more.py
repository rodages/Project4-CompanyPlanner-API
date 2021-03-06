# Generated by Django 4.0.4 on 2022-05-07 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Checklists', '0003_remove_checklist_amount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shifts', '0005_alter_shift_checklist_alter_shift_checklists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='completed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='section_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='checklist',
            field=models.ManyToManyField(blank=True, related_name='items', to='Shifts.checklistitem'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='checklists',
            field=models.ManyToManyField(blank=True, related_name='shifts', to='Checklists.checklist'),
        ),
    ]
