from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', "f_name", "l_name")

class AddEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("f_name", "l_name")