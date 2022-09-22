from dataclasses import field
from rest_framework import serializers
from portal.models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ("__all__")

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['email', 'name', 'contact', 'gender', 'age']
