from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'description', 'created_at', 'updated_at']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.created_at = validated_data.get('created_at',
                                                 instance.created_at)
        instance.updated_at = validated_data.get('updated_at',
                                                 instance.updated_at)
        instance.save()
        return instance
