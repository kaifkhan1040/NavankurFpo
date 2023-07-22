# Generated by Django 3.2 on 2022-07-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_fpo_passbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fpobankdetails',
            name='bank_statement_doc',
        ),
        migrations.RemoveField(
            model_name='fpobankdetails',
            name='passbook_doc',
        ),
        migrations.AddField(
            model_name='fpobankdetails',
            name='authorised_person',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
