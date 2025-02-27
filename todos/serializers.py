from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["todoId", "user", "createDate"]

    def create(self, validated_data):
        
        validated_data.pop("description", None)
        validated_data.pop("todoImage", None)
        return super().create(validated_data)

#어차피 프론트에서 투두 작성할때 상세설명이랑 이미지는 처음에는 못쓰고 수정에서 쓸 수 있게 할거라서
#굳이 이거 안해도 되는데 이렇게 한건....그냥 해봄;; ㅇㅇ 주소창에 끼워서 쓰면 들어가버릴수있잖슴.
#암튼 여기서 설정해준게, 설명이랑 이미지 들어와도 pop하고 날라가버림.