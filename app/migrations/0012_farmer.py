# Generated by Django 3.2 on 2022-06-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220621_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_holder_name', models.CharField(max_length=15)),
            ],
        ),
    ]
