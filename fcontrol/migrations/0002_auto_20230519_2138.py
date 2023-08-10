# Generated by Django 3.2.18 on 2023-05-19 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fcontrol', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controller',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='controller',
            name='temperature',
        ),
        migrations.CreateModel(
            name='ControllerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='температура')),
                ('humidity', models.PositiveSmallIntegerField(verbose_name='Влажность')),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='fcontrol.controller')),
            ],
        ),
    ]