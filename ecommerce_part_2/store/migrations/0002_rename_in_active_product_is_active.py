# Generated by Django 4.2 on 2023-04-20 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='in_active',
            new_name='is_active',
        ),
    ]