# Generated by Django 3.0 on 2022-05-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fpo',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
