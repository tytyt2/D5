# Generated by Django 4.2.2 on 2023-08-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='added_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
