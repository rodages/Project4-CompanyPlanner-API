# Generated by Django 4.0.4 on 2022-05-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shifts', '0006_alter_checklistitem_completed_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistitem',
            name='assigned_to',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='checklistitem',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]