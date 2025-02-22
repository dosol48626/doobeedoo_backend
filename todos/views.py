from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from datetime import date
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        - 로그인 유저의 Todo만
        - priority가 주어지면 미완료(complete=False)이면서 해당 priority만
        - query(검색어) 파라미터가 있으면 제목/내용에 검색
        """
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)

        routine_id = self.request.query_params.get('routine')
        if routine_id:
            qs = qs.filter(routine=routine_id)

        # 중요도 필터 (만약 ?priority=RED 라면, RED & 미완료인 것만)
        priority = self.request.query_params.get('priority')
        if priority:
            qs = qs.filter(priority=priority, complete=False)

        # 검색어 필터 (완료/미완료 구분 없이)
        query = self.request.query_params.get('query')
        if query:
            qs = qs.filter(title__icontains=query) | qs.filter(description__icontains=query)

        return qs

    def perform_create(self, serializer):
        """
        - 생성 시 user 필드를 현재 사용자로 설정
        - description과 todoImage는 serializer가 제거하므로 여기선 신경 안씀
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='today')
    def today_todos(self, request):
        """
        오늘의 투두: dueDate == today
        """
        today = date.today()
        qs = self.get_queryset().filter(dueDate=today)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='next')
    def next_todos(self, request):
        """
        '오늘이 아닌' 모든 투두 보여주기 (dueDate != today)
        """
        today = date.today()
        qs = self.get_queryset().exclude(dueDate=today)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='toggle')
    def toggle_complete(self, request, pk=None):
        """
        토글 기능: complete = not complete
        POST /api/todos/<id>/toggle/
        """
        todo = self.get_object()  # detail=True -> 특정 객체를 가져옴
        todo.complete = not todo.complete
        todo.save()
        return Response(
            {"message": "토글 완료", "complete": todo.complete},
            status=status.HTTP_200_OK
        )
