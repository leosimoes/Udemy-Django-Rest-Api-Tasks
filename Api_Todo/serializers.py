from Api_Todo.models import Task

from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta():
        model = Task
        fields = ['id', 'name', 'done', 'created_at']
        # fields = '__all__'