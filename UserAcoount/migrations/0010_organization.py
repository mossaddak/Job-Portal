# Generated by Django 4.2.4 on 2023-09-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0009_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
