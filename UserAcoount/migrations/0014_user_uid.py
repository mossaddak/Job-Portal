# Generated by Django 4.2.4 on 2023-09-04 18:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0013_remove_user_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
