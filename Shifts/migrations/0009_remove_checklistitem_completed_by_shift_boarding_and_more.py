# Generated by Django 4.0.4 on 2022-05-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shifts', '0008_rename_count_checklistitem_extra_from_checklist_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklistitem',
            name='completed_by',
        ),
        migrations.AddField(
            model_name='shift',
            name='boarding',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='dropoff',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='leaving_pier',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
