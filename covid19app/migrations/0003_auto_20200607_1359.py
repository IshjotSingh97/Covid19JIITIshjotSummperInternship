# Generated by Django 3.0.2 on 2020-06-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19app', '0002_auto_20200607_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myth',
            name='img',
        ),
        migrations.AddField(
            model_name='myth',
            name='subject',
            field=models.TextField(default='Default', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]