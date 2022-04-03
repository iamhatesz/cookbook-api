from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from cookbook_api.api.models import Recipe, Tag


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class RecipeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ["name", "description", "tags"]

    tags = TagSerializer(many=True)


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups", "first_name", "last_name"]
