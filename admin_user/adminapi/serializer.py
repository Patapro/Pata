from django.contrib.auth.models import User
from rest_framework import serializers

from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers


class AdminloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
