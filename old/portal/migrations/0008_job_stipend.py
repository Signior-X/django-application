# Generated by Django 4.1.1 on 2022-09-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_alter_application_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='stipend',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
