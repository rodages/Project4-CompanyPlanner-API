# Generated by Django 4.0.4 on 2022-05-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=30)),
                ('last_name', models.CharField(default=None, max_length=50)),
                ('role', models.CharField(default=None, max_length=30)),
                ('postcode', models.CharField(default=None, max_length=10)),
                ('active', models.BooleanField(default=False)),
                ('registeredAt', models.DateField(auto_now=True, null=True)),
                ('updatedAt', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]