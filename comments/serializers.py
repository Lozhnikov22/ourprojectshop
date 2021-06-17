from rest_framework import serializers

from comments.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    # post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Feedback
        fields = ('id', 'body', 'author', 'product')

