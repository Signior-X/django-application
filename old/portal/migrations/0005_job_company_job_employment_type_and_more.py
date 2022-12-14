# Generated by Django 4.1.1 on 2022-09-21 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_alter_applicant_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='job',
            name='employment_type',
            field=models.CharField(choices=[('FT', 'Full-time'), ('IN', 'Internship'), ('PT', 'Part-time')], default='FT', max_length=2),
        ),
        migrations.AlterField(
            model_name='application',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
