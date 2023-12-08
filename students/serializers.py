from rest_framework import serializers
from task.models.task import *
from .models import *


class StudentsSerializer(serializers.ModelSerializer):
    answer_count = serializers.SerializerMethodField()
    class Meta:
        model = Student
        # fields = "__all__"
        fields = ['user', 'phone_number','programming_language','answer_count']

    def get_answer_count(self, student_obj):
        return student_obj.answer_list.count()

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['phone_number','programming_language']