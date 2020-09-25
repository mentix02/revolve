from rest_framework import serializers

from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'
