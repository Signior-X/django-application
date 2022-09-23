# Generated by Django 4.1.1 on 2022-09-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Mentioned', 'Not Mentioned')], default='Not Mentioned', max_length=32),
        ),
        migrations.AddField(
            model_name='applicant',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]