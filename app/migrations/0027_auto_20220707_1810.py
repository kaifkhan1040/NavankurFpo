# Generated by Django 3.2 on 2022-07-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_fpo_fpo_post_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberdetails',
            name='category',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriberdetails',
            name='gender',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]