from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ('id','title', 'slug', 'about', 'content','image', 'created','status', 'author')
        read_only_fields = ('id', 'created', 'status')

    def create(self, validated_data):
        blog = super().create(validated_data)
        blog.author = self.context['user']
        blog.save()
        return blog

