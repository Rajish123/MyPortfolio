# Generated by Django 4.1.2 on 2022-10-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumVitae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='CV')),
            ],
        ),
    ]
