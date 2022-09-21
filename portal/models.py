from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

import uuid


class Applicant(models.Model):
    '''
    Applicant that is applying for the job
    having a particular id
    '''

    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=64)
    contact = models.BigIntegerField(blank=True, null=True)


class Job(models.Model):
    '''
    Suppose the job that someone has posted.
    For simplicity, we will use id for login
    '''

    class EmploymentType(models.TextChoices):
        FULL_TIME = 'FT', _('Full-time')
        INTERNSHIP = 'IN', _('Internship')
        PART_TIME = 'PT', _('Part-time')

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    company = models.CharField(max_length=64, default='', name="company")

    # role can be like Full-stack developer, frontend developer
    role = models.CharField(max_length=64, name="role")

    # The md formated description for the role
    desc = models.TextField(name="desc")

    employment_type = models.CharField(
        max_length=2,
        choices=EmploymentType.choices,
        default=EmploymentType.FULL_TIME)

    remote = models.BooleanField(default=False)

    # For storing compensation
    stipend = models.IntegerField(blank=True, null=True)


class Application(models.Model):
    '''
    Application details for a particular applicant linking
    to a particular job
    '''

    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created']


# class Address(models.Model):
#     ''' Adress Class to store objects '''

#     country = models.CharField(default="India")
#     pincode = models.IntegerField()

#     state = models.CharField(max_length=256)
#     city = models.CharField(max_length=256)
#     street = models.TextField()
