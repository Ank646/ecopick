# Generated by Django 4.2.5 on 2023-11-12 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("connect", "0002_userpro_email_token"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userpro",
            old_name="user",
            new_name="user_id",
        ),
    ]
