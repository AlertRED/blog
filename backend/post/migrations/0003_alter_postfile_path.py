# Generated by Django 4.0.4 on 2022-08-23 12:16

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile',
            name='path',
            field=models.FileField(blank=True, default='none', upload_to=post.models.post_file_name, verbose_name='Путь к файлу'),
            preserve_default=False,
        ),
    ]