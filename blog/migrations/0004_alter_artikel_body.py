# Generated by Django 4.1.2 on 2022-12-22 11:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_artikel_nama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
