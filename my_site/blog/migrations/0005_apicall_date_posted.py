# Generated by Django 3.2.5 on 2021-07-14 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_apicall_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='apicall',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
