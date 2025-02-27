from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Routine
from .serializers import RoutineSerializer

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 현재 로그인 사용자의 루틴만 보이게
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        # 루틴 만들 때 user 자동 할당
        serializer.save(user=self.request.user)

#여기도 viewset으로해서 썻고. 근데 솔직히 viewset이 어떻게 작동하는건지 내부적으로 다 이해는 못함.
#일단 내가 쟝고 쓰는 이유가 이거였음. APIVIEW랑 VIESET. 이렇게 하면 부트보다 훨씬 빠르니까.