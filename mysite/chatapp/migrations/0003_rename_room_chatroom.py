# Generated by Django 4.2.2 on 2023-06-17 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_rename_rooms_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='ChatRoom',
        ),
    ]