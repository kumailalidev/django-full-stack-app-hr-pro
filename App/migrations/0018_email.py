# Generated by Django 4.2.5 on 2023-09-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_alter_candidate_databases_alter_candidate_frameworks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]