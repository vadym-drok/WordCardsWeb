# Generated by Django 3.2 on 2021-04-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_word_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.ImageField(blank=True, default='../images/default.jpg', upload_to='../images/'),
        ),
    ]