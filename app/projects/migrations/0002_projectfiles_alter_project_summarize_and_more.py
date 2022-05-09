# Generated by Django 4.0.4 on 2022-04-13 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/None/')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='summarize',
            field=models.CharField(help_text='80 caractères max', max_length=80, verbose_name='Resumer'),
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
        migrations.AddField(
            model_name='projectfiles',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
