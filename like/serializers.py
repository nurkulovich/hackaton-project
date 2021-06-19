from rest_framework import serializers

from food.models import Food
from like.models import Like, DisLike


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ("owner", "likes_number")


class DisLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = DisLike
        fields = ("owner", "dislikes_number",)
