from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoScoreView

# ✅ score 경로를 먼저 선언
urlpatterns = [
    path('score/', TodoScoreView.as_view(), name='todo-score'),  # 이걸 먼저!
]

# ✅ 그 다음에 router 등록
router = DefaultRouter()
router.register('', TodoViewSet, basename='todo')

urlpatterns += [
    path('', include(router.urls)),
]

# 점수 조회:
# GET /api/todos/score/

# 투두 목록 조회:
# GET /api/todos/

# 오늘의 투두 조회:
# GET /api/todos/today/

# 다음 투두 조회:
# GET /api/todos/next/

# 투두 생성:
# POST /api/todos/

# 투두 상세 조회:
# GET /api/todos/{todoId}/

# 투두 수정:
# PUT /api/todos/{todoId}/

# 투두 완료 토글:
# POST /api/todos/{todoId}/toggle/

# 중요도별 조회:
# GET /api/todos/?priority=RED
# GET /api/todos/?priority=BLUE
# GET /api/todos/?priority=YELLOW
# GET /api/todos/?priority=BLACK

# 투두 검색:
# GET /api/todos/?query=검색어
