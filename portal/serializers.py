from dataclasses import field, fields
from rest_framework import serializers
from portal.models import Applicant

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ("__all__")

class ApplicantStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['email', 'status']

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['email', 'name', 'contact', 'gender', 'age', 'status', 'field_of_study']
