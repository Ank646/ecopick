# Generated by Django 4.2.5 on 2023-11-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("connect", "0003_rename_user_userpro_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userpro",
            old_name="user_id",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="userpro",
            name="email_token",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
