from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path(
        '',
        views.RecipeListViewHome.as_view(),
        name='home'
    ),
    path(
        'recipes/search/',
        views.RecipeListViewSearch.as_view(),
        name='search'
    ),
    path(
        'recipes/tags/<slug:slug>/',
        views.RecipeListViewTag.as_view(),
        name='tag'
    ),
    path(
        'recipes/category/<int:category_id>/',
        views.RecipeListViewCategory.as_view(),
        name='category'
    ),
    path(
        'recipes/<int:pk>/',
        views.RecipeDetails.as_view(),
        name='recipe'
    ),
    path(
        'recipes/api/v1/',
        views.RecipeListViewHomeApi.as_view(),
        name='recipes_api_v1'
    ),
    path(
        'recipes/api/v1/<int:pk>/',
        views.RecipeDetailsApi.as_view(),
        name='recipes_api_v1_detail',
    ),
    path(
        'recipes/api/v2/',
        views.recipe_api_list,
        name='recipes_api_v2',
    ),

]
