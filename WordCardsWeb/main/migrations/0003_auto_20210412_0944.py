# Generated by Django 3.1.8 on 2021-04-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210408_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=200),
        ),
    ]