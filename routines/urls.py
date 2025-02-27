from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutineViewSet

router = DefaultRouter()
router.register('', RoutineViewSet, basename='routine')

urlpatterns = [
    path('', include(router.urls)),
]



# 루틴 생성: POST /api/routines/ → {"name": "아침 루틴"}
# 전체 조회: GET /api/routines/
# 상세 조회: GET /api/routines/1/
# 수정: PUT /api/routines/1/ → {"name": "아침 스트레칭"}
# 삭제: DELETE /api/routines/1/
# 루틴 투두 조회: GET /api/todos/?routine=1