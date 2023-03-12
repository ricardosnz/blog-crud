from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog

class BlogsAPIView(APIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.filter(status=True)
  def get(self, request, *args, **kwargs):
    blogs = self.queryset
    if blogs.exists():
      blogs_serializer = self.serializer_class(blogs, many=True)
      return Response(blogs_serializer.data, status)
    return Response()
  def post(self, request, *args, **kwargs):
    blog_serializer = self.serializer_class(data=request.data)
    if blog_serializer.is_valid():
      blog_serializer.save()
      return Response(blog_serializer.data, status=status.HTTP_201_CREATED)
    return Response(blog_serializer.errors)

class BlogAPIView(APIView):
  serializer_class = BlogSerializer
  queryset = Blog.objects.filter(status=True)

  def get_object(self, pk):
    blog = self.queryset.filter(pk=pk)
    if blog.exists():
      return blog.get()
    return Response({'msg': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)  
  
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
    blog.stauts=False
    blog.save()
    return Response(status=status.HTTP_200_OK)
  

