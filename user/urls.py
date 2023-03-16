from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginUserTokenObtainView, RegisterUserTokenObtainView, EditUserAPIView, LogoutUserAPIView

app_name = 'user'
urlpatterns = [
    path('login/', LoginUserTokenObtainView.as_view(), name='login'),
    path('register/', RegisterUserTokenObtainView.as_view(), name='register'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
    path('edit/', EditUserAPIView.as_view(), name='edit')
]

