# Generated by Django 2.1.3 on 2018-11-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20181116_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opsserver',
            name='online_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='投产时间'),
        ),
    ]