from django.urls import path
from .views import BlogsAPIView, BlogAPIView

app_name = 'blog'

urlpatterns = [
    path('', BlogsAPIView.as_view(), name='blogs'),
    path('<int:pk>/', BlogAPIView.as_view(), name='blog'),
]