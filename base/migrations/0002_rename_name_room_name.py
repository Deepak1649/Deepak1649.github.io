# Generated by Django 4.1.7 on 2023-08-05 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='Name',
            new_name='name',
        ),
    ]
