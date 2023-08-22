from rest_framework import serializers ,status
from app import models


class StudentSerializers(serializers.ModelSerializer):
    Password = serializers.CharField(max_length=250,style={'input_type':'password','placeholder':'password'})
    class Meta:
        model = models.Student
        fields = ['email','Password']