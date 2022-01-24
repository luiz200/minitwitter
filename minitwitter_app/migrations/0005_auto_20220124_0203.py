# Generated by Django 3.0.5 on 2022-01-24 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('minitwitter_app', '0004_remove_public_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='public',
            name='file',
            field=models.ImageField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='public',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
