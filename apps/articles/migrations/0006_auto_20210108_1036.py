# Generated by Django 3.1.4 on 2021-01-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210108_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='%Y%m%d/', verbose_name='文章配图'),
        ),
    ]