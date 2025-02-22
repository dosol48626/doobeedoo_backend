from django.urls import path
from .views import RegisterView
from .views import LoginView
from .views import LogoutView
from .views import PasswordChangeView
from .views import DeleteAccountView
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('delete_account/', DeleteAccountView.as_view(), name='delete_account'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
