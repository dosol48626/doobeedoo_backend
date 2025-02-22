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
