from dataclasses import fields
from rest_framework import serializers
from portal.models import Applicant, Job
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['email', 'name', 'contact']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("__all__")
    