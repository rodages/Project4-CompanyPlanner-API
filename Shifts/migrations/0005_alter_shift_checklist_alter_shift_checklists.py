# Generated by Django 4.0.4 on 2022-05-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checklists', '0003_remove_checklist_amount'),
        ('Shifts', '0004_alter_shift_checklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='checklist',
            field=models.ManyToManyField(blank=True, null=True, related_name='items', to='Shifts.checklistitem'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='checklists',
            field=models.ManyToManyField(blank=True, null=True, related_name='shifts', to='Checklists.checklist'),
        ),
    ]
