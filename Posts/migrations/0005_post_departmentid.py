# Generated by Django 4.0.4 on 2022-05-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_alter_post_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='departmentID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
