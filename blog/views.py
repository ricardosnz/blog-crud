from django.db.models.query_utils import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BlogSerializer
from .pagination import SetPagination
from .models import Blog

class BlogsAPIView(APIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.filter(status=True)
  authentication_classes = [JWTAuthentication]
  pagination_class = SetPagination

  def query_param(self, request):
    search = self.request.GET.get('q', None)
    if search is None:
      return self.queryset.all()
    return Blog.objects.filter(Q(title__icontains=search)|Q(content__icontains=search)|Q(about__icontains=search))

  def get(self, request, *args, **kwargs):
    blogs = self.query_param(request)
    if blogs.exists():
      paginator = self.pagination_class()
      results = paginator.paginate_queryset(blogs, request)
      blogs_serializer = self.serializer_class(results, many=True)
      return Response(blogs_serializer.data)
    return Response({'menssage': "No results"}, status=status.HTTP_404_NOT_FOUND)
  def post(self, request, *args, **kwargs):
    blog_serializer = self.serializer_class(data=request.data, context={'user':request.user})
    if blog_serializer.is_valid():
      blog_serializer.save()
      return Response(blog_serializer.data, status=status.HTTP_201_CREATED)
    return Response(blog_serializer.errors)

class BlogAPIView(APIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.filter(status=True)
  authentication_classes = [JWTAuthentication]

  def get_object(self, pk):
    blog = self.queryset.filter(pk=pk) 
    if blog.exists():
      return blog.get()
    
  def get(self, request, pk, *args, **kwargs):
    blog = self.get_object(pk)
    blog_serializer = self.serializer_class(blog)
    return Response(blog_serializer.data)
  def put(self, request, pk, *args, **kwargs):
    blog = self.get_object(pk)
    blog_serializer = self.serializer_class(blog, data=request.data)
    if blog_serializer.is_valid():
      blog_serializer.save()
      return Response(blog_serializer.data,status=status.HTTP_200_OK)
    return Response(blog_serializer.errors)
  def delete(self, request, pk, *args, **kwargs):
    blog = self.get_object(pk)
    blog.status=False
    blog.save()
    return Response(status=status.HTTP_200_OK)
  

