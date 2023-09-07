# Generated by Django 4.2.5 on 2023-09-07 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_remove_candidate_age_candidate_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='about_course',
            field=models.TextField(default=datetime.datetime(2023, 9, 7, 12, 12, 54, 390358, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='about_job',
            field=models.TextField(default=datetime.datetime(2023, 9, 7, 12, 13, 6, 486406, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='company',
            field=models.CharField(default=datetime.datetime(2023, 9, 7, 12, 13, 9, 542954, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='course',
            field=models.CharField(default=datetime.datetime(2023, 9, 7, 12, 13, 14, 278448, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='employed',
            field=models.BooleanField(null=True, verbose_name='I am employed'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='finished_course',
            field=models.DateField(default=datetime.datetime(2023, 9, 7, 12, 13, 19, 302355, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='finished_job',
            field=models.DateField(default=datetime.datetime(2023, 9, 7, 12, 13, 22, 631177, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='institution',
            field=models.CharField(default=datetime.datetime(2023, 9, 7, 12, 13, 24, 934241, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.CharField(default=datetime.datetime(2023, 9, 7, 12, 13, 29, 150188, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='remote',
            field=models.BooleanField(null=True, verbose_name='I agree to work remotely'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='started_course',
            field=models.DateField(default=datetime.datetime(2023, 9, 7, 12, 13, 32, 679033, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='started_job',
            field=models.DateField(default=datetime.datetime(2023, 9, 7, 12, 13, 35, 519112, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='status_course',
            field=models.CharField(choices=[('', 'Select your status'), ("I'm studying", "I' am studying"), ('I took a break', 'I took a break'), ('Completed', 'Completed')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='travel',
            field=models.BooleanField(null=True, verbose_name="I'm available for travel"),
        ),
    ]