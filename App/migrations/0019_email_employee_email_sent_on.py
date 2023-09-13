# Generated by Django 4.2.5 on 2023-09-13 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='employee',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='sent_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
