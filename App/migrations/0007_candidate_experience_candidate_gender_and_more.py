# Generated by Django 4.2.5 on 2023-09-04 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_candidate_situation'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(default=datetime.datetime(2023, 9, 4, 23, 14, 41, 584800, tzinfo=datetime.timezone.utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='personality',
            field=models.CharField(choices=[('', 'Select a personality'), ('I am outgoing', 'I am outgoing'), ('I am sociable', 'I am sociable'), ('I am antisocial', 'I am antisocial'), ('I am discrete', 'I am discrete'), ('I am serious', 'I am serious')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='salary',
            field=models.CharField(default=datetime.datetime(2023, 9, 4, 23, 15, 25, 736918, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='smoker',
            field=models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='', max_length=10),
        ),
    ]
