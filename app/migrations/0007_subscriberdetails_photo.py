# Generated by Django 3.2 on 2022-06-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_ia_subscriberdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberdetails',
            name='photo',
            field=models.ImageField(default=1, upload_to='subscriberdetails/'),
            preserve_default=False,
        ),
    ]