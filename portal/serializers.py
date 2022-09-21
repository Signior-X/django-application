from dataclasses import fields
from rest_framework import serializers
from portal.models import Applicant, Job

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['email', 'name', 'contact']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("__all__")
    