# Generated by Django 4.0.4 on 2022-05-12 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_customuser_dob_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(default=datetime.date(2022, 5, 12)),
        ),
    ]
