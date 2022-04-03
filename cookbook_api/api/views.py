from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from cookbook_api.api.models import Recipe
from cookbook_api.api.serializers import RecipeSerializer


class RecipeViewSet(ReadOnlyModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = []


class UserRecipeViewSet(ReadOnlyModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.user.id)
