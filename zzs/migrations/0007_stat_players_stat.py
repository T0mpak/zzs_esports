# Generated by Django 3.0.5 on 2020-05-02 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zzs', '0006_auto_20200502_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='players_stat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.MostValuablePlayer', verbose_name='Статистика игрока'),
        ),
    ]
