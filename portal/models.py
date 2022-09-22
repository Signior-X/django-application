from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Applicant(models.Model):
    '''
    Applicant that is applying for the job
    having a particular id
    '''

    class Gender(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        NOT_MENTIONED = "Not Mentioned"

    class StudiedUpto(models.TextChoices):
        HIGH_SCHOOL = 'High School'
        BACHELORS = 'Bachelors'
        MASTERS = 'Masters'
        DOCTORATE = 'Doctorate'

    class ApplicantStatus(models.TextChoices):
        INCOMPLETE = "Incomplete"
        SUBMITTED = "Submitted"
        REJECTED = "Rejected"
        ACCEPTED = "Accepted"


    name = models.CharField(max_length=256, default="")
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=32,
        choices=Gender.choices,
        default=Gender.NOT_MENTIONED
    )

    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(primary_key=True)

    # All related data for the candidate will be here
    contact = models.PositiveBigIntegerField(blank=True, null=True)

    degree = models.CharField(
        max_length=32,
        choices=StudiedUpto.choices,
        default=StudiedUpto.HIGH_SCHOOL)

    field_of_study = models.CharField(max_length=256)

    # Timestamp when he applied
    timestamp = models.DateTimeField(default=timezone.now)

    # status of the applicant
    status = models.CharField(
        max_length=32,
        choices=ApplicantStatus.choices,
        default=ApplicantStatus.INCOMPLETE
    )

