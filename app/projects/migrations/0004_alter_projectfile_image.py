# Generated by Django 4.0.4 on 2022-04-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_projectfiles_projectfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='image',
            field=models.ImageField(upload_to='projects/<function get_upload_path at 0x7fcbc0e3a940>/'),
        ),
    ]
