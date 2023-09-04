# Generated by Django 4.2.4 on 2023-08-27 16:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0004_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]