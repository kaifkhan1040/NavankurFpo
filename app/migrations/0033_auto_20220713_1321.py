# Generated by Django 3.2 on 2022-07-13 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20220713_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fpo',
            name='fpo_ceo_education_documents',
        ),
        migrations.CreateModel(
            name='FpoCeoEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=50)),
                ('education_documents', models.ImageField(upload_to='fpo_accountant/fpo_accountant_education_documents/')),
                ('fpo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fpo')),
            ],
        ),
    ]
