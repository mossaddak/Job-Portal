# Generated by Django 4.2.4 on 2023-09-04 18:31

import UserAcoount.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0015_organization_organizationuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='image',
            field=models.ImageField(null=True, upload_to=UserAcoount.models.upload_to_organization_image),
        ),
    ]
