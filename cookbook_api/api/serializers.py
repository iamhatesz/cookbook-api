from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from cookbook_api.api.models import Recipe, Tag


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class RecipeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ["name", "description", "instructions", "tags", "author", "created_on"]

    author = UserSerializer()
    tags = TagSerializer(many=True)

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        recipe = Recipe.objects.create(**validated_data)
        for tag_id in tags_data:
            tag = Tag.objects.get(name=tag_id["name"])
            recipe.tags.add(tag)
        return recipe
