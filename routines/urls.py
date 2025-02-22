from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoutineViewSet

router = DefaultRouter()
router.register('', RoutineViewSet, basename='routine')

urlpatterns = [
    path('', include(router.urls)),
]
