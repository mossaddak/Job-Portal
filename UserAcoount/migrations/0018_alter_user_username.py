# Generated by Django 4.2.4 on 2023-09-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0017_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
