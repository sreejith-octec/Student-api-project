from rest_framework import serializers
from .models import Student, Mark
   

class MarkSerializer(serializers.ModelSerializer):
    """Serialize mark detail"""

    class Meta:
        model = Mark
        fields = '__all__'
        read_only_fields = ('id',)


class StudentSerializer(serializers.ModelSerializer):
    """Serialize a student detail"""

    class Meta:
        model = Student
        fields = ('id','name', 'roll_number', 'date_of_birth')
        read_only_fields = ('id',)
