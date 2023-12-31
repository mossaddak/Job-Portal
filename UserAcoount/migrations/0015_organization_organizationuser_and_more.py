# Generated by Django 4.2.4 on 2023-09-04 18:29

import UserAcoount.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0014_user_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=UserAcoount.models.upload_to_user_profile_image)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PLACEHOLDER', 'Placeholder'), ('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('HIDDEN', 'Hidden'), ('REMOVED', 'Removed')], db_index=True, default='DRAFT', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('OWNER', 'Owner'), ('ADMIN', 'Admin'), ('HR', 'Human Resource'), ('APPLICANT', 'Applicant')], max_length=20)),
                ('status', models.CharField(choices=[('INVITED', 'Invited'), ('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('SUSPEND', 'Suspend'), ('REJECTED', 'Rejected'), ('DEACTIVATE', 'Deactivate'), ('HIDDEN', 'Hidden'), ('REMOVED', 'Removed')], default='PENDING', max_length=20)),
                ('is_default', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAcoount.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='organizationuser',
            constraint=models.UniqueConstraint(condition=models.Q(('is_default', True)), fields=('user',), name='user_have_one_default_organization', violation_error_message='A merchant can have only one default organization.'),
        ),
    ]
