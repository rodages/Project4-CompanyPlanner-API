# Generated by Django 4.0.4 on 2022-05-05 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryItems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]