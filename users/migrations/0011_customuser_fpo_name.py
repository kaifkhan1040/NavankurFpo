# Generated by Django 3.0 on 2022-06-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220524_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fpo_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
