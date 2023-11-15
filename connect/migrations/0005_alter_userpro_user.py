# Generated by Django 4.2.5 on 2023-11-12 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("connect", "0004_rename_user_id_userpro_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpro",
            name="user",
            field=models.OneToOneField(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]