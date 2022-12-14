# Generated by Django 4.1.1 on 2022-09-21 06:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_applicant_name_alter_job_desc_alter_job_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='id',
        ),
        migrations.AddField(
            model_name='applicant',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.applicant')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.job')),
            ],
        ),
    ]
