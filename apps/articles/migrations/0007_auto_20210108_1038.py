# Generated by Django 3.1.4 on 2021-01-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20210108_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='%Y%m%d%H%M%S/', verbose_name='文章配图'),
        ),
    ]