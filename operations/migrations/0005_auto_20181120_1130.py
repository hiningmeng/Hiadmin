# Generated by Django 2.1.3 on 2018-11-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0004_auto_20181116_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='opshost',
            name='use_port1',
            field=models.CharField(max_length=50, null=True, verbose_name='使用的端口'),
        ),
        migrations.AddField(
            model_name='opshost',
            name='use_port2',
            field=models.CharField(max_length=50, null=True, verbose_name='使用的端口'),
        ),
        migrations.AddField(
            model_name='opshost',
            name='use_port3',
            field=models.CharField(max_length=50, null=True, verbose_name='使用的端口'),
        ),
        migrations.AddField(
            model_name='opshost',
            name='use_port4',
            field=models.CharField(max_length=50, null=True, verbose_name='使用的端口'),
        ),
    ]
