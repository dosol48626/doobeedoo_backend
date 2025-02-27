from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView

from datetime import date
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)

        routine_id = self.request.query_params.get('routine')
        if routine_id:
            qs = qs.filter(routine=routine_id)

        priority = self.request.query_params.get('priority')
        if priority:
            qs = qs.filter(priority=priority, complete=False)

        query = self.request.query_params.get('query')
        if query:
            qs = qs.filter(title__icontains=query) | qs.filter(description__icontains=query)

        return qs

    def perform_create(self, serializer):
       
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='today')
    def today_todos(self, request):
  
        today = date.today()
        qs = self.get_queryset().filter(dueDate=today)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='next')
    def next_todos(self, request):
    
        today = date.today()
        qs = self.get_queryset().exclude(dueDate=today)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='toggle')
    def toggle_complete(self, request, pk=None):
    
        todo = self.get_object()
        todo.complete = not todo.complete
        todo.save()
        return Response(
            {"message": "토글 완료", "complete": todo.complete},
            status=status.HTTP_200_OK
        )

class TodoScoreView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        completed_todos = Todo.objects.filter(user=user, complete=True).count()
        score = completed_todos * 2 
        return Response({"score": score})
    
