# Generated by Django 2.1.3 on 2018-11-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navi',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
    ]
