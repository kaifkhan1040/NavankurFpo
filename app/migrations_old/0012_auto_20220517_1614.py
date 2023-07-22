# Generated by Django 3.0 on 2022-05-17 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20220517_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='fpo',
            name='district',
            field=models.ForeignKey(default=36, on_delete=django.db.models.deletion.CASCADE, to='app.District'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fpo',
            name='implementing_agency',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fpo',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fpo',
            name='state_category',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
    ]