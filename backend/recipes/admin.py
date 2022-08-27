from django.contrib import admin

from .models import (
    Favorite,
    Ingredient,
    IngredientRecipe,
    Recipe,
    ShoppingCart,
    Tag
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


class IngredientRecipeInline(admin.TabularInline):
    model = IngredientRecipe


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author')
    search_fields = ('author', 'name', 'tags')
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientRecipeInline,)
    readonly_fields = ('favorites_count',)
    empty_value_display = '-пусто-'

    def favorites_count(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@admin.register(IngredientRecipe)
class IngredientRecipeAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'amount')
    list_filter = ('ingredient', 'recipe', 'amount')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user', 'recipe',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
