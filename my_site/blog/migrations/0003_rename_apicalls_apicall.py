# Generated by Django 3.2.5 on 2021-07-13 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_apicalls'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApiCalls',
            new_name='ApiCall',
        ),
    ]
