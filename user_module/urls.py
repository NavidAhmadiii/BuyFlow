from django.urls import path
from .views import LoginAPIView, UserRegisterAPIView, ProfileAPIView, ProfileDetailAPIView, TokenRefreshAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login_api'),
    path('register/', UserRegisterAPIView.as_view(), name='user_register_api'),
    path('profile/', ProfileAPIView.as_view(), name='profile_api'),
    path('profile/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile_api'),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh_api')
]
