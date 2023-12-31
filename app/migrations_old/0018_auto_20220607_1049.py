# Generated by Django 3.0 on 2022-06-07 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220530_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fpo',
            options={'verbose_name_plural': 'fpo'},
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
        migrations.AlterField(
            model_name='farmer',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
        migrations.AlterField(
            model_name='fpo',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District'),
        ),
        migrations.AlterField(
            model_name='fpo',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.State'),
        ),
    ]
