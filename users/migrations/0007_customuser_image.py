# Generated by Django 3.0 on 2022-05-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_forgetpassmailverify'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='user_profile/'),
        ),
    ]