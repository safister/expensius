# Generated by Django 3.0.4 on 2020-03-07 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]