# Generated by Django 3.0.5 on 2020-05-15 14:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200515_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='内容', max_length=1500, verbose_name='内容'),
        ),
    ]