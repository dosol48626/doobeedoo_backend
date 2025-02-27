from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/todos/', include('todos.urls')),
    path('api/routines/', include('routines.urls')),
]

#나중에 배포할때는 바꿔야함.
#Django에서 권장하는 표준 방식으로, 
# 개발 환경(DEBUG=True)에서만 미디어 파일을 처리하도록 설정하는 방법
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
