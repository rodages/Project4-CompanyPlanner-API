# Generated by Django 4.0.4 on 2022-05-04 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryItems', '0001_initial'),
        ('Subsections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsection',
            name='inventory_items',
            field=models.ManyToManyField(blank=True, related_name='subsection_item', to='InventoryItems.inventoryitem'),
        ),
    ]