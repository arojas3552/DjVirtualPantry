# Generated by Django 3.2.9 on 2023-08-02 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('virtualPantry_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='food',
        ),
    ]
