# Generated by Django 4.1.1 on 2022-09-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='job',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='role',
            field=models.CharField(max_length=64),
        ),
    ]
