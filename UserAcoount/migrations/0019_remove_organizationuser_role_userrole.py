# Generated by Django 4.2.4 on 2023-09-06 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAcoount', '0018_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationuser',
            name='role',
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('OWNER', 'Owner'), ('ADMIN', 'Admin'), ('HR', 'Human Resource'), ('APPLICANT', 'Applicant')], max_length=20)),
                ('organization_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserAcoount.organizationuser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
