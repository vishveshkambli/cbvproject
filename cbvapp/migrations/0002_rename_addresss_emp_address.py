# Generated by Django 4.2.5 on 2023-10-29 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='addresss',
            new_name='address',
        ),
    ]