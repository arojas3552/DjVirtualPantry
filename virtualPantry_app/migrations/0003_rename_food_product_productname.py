# Generated by Django 3.2.9 on 2023-08-02 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virtualPantry_app', '0002_rename_productname_product_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='food',
            new_name='productName',
        ),
    ]
