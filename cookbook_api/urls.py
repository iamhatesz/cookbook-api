"""cookbook_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as authtoken_views

from cookbook_api.api.views import RecipeViewSet, UserRecipeViewSet

router = DefaultRouter()
router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"user/recipes", UserRecipeViewSet, basename="user_recipes")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api-token-auth/', authtoken_views.obtain_auth_token),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
