from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["todoId", "user", "createDate"]

    def create(self, validated_data):
        """
        생성 시에는 title, dueDate, priority만 허용.
        description과 todoImage는 무시함.
        """
        validated_data.pop("description", None)
        validated_data.pop("todoImage", None)
        return super().create(validated_data)
