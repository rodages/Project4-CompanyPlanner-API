# Generated by Django 4.0.4 on 2022-05-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checklists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
