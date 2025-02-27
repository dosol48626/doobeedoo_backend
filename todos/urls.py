from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoScoreView

urlpatterns = [
    path('score/', TodoScoreView.as_view(), name='todo-score'),
]
#이거는 APIVIEW써서 이거 해줘야함. 그리고 몰랐는데 이거를 맨위로 올려줘야 작동을 하네;;

router = DefaultRouter()
router.register('', TodoViewSet, basename='todo')

urlpatterns += [
    path('', include(router.urls)),
]
#urlpatterns이 두개인 이유는 위에꺼는 APIVIEW고 밑에꺼는 VIEWSET이기 때문임.

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
