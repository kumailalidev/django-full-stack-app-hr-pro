# Generated by Django 4.2.5 on 2023-09-14 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0021_alter_candidate_started_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_email', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('chat', models.CharField(max_length=500)),
                ('dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
