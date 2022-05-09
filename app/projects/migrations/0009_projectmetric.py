# Generated by Django 4.0.4 on 2022-04-13 16:38

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_projectimage_delete_projectfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewer_month', models.CharField(max_length=50, verbose_name='Visiteur par mois')),
                ('viewer_proof', models.ImageField(upload_to=projects.models.get_upload_path)),
                ('download_month', models.CharField(max_length=200, verbose_name='Nombre de téléchargement')),
                ('download_proof', models.ImageField(upload_to=projects.models.get_upload_path)),
                ('revenue_month', models.CharField(max_length=200, verbose_name='Revenue mensuel')),
                ('revenue_proof', models.ImageField(upload_to=projects.models.get_upload_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='projects.project')),
            ],
        ),
    ]
