from rest_framework import serializers
from reviews.models import Review, Comments


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
