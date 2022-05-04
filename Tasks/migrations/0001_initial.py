# Generated by Django 4.0.4 on 2022-05-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_name', models.CharField(default=None, max_length=200, null=True)),
                ('comments', models.CharField(default=None, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]