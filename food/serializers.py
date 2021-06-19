from rest_framework import serializers
from food.models import Food, Category
from like.models import Like
from review.models import Review, Mark
from django.db.models import Avg
from review.serializers import ReviewDetailSerializer, MarkSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation


class FoodSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Food
        fields = ['preview', 'title', 'composition', 'price', 'category']

    def create(self, validated_data):
        print(validated_data)
        request = self.context.get('request')
        images_data = request.FILES
        created_post = Food.objects.create(**validated_data)
        print(created_post)
        images_obj = [
            Food(post=created_post, image=image)
            for image in images_data.getlist('images')
        ]
        Food.objects.bulk_create(images_obj)
        return created_post

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['review_count'] = f'{Review.objects.filter(food=instance.id).count()}'
        representation['like_count'] = f'{Like.objects.filter(food=instance.id).count()}'
        representation['marks'] = Mark.objects.all().aggregate(Avg('mark'))
        return representation


class FoodDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['preview', 'title', 'composition', 'price', 'category']

    def to_representation(self, instance):
        representation = super(FoodDetailSerializer, self).to_representation(instance)
        representation['review'] = ReviewDetailSerializer(Review.objects.filter(food=instance.id), many=True).data
        representation['marks'] = MarkSerializer(Mark.objects.filter(food=instance.id), many=True).data
        return representation


